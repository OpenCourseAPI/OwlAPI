import sys
from os import makedirs, rename, remove
from os.path import join, exists
from collections import defaultdict
import re

# 3rd party
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB
from colorama import init, Fore, Style
from selenium_login import scrape_cookies, kill_driver

from settings import DB_DIR, ADVANCED_FORM_DATA

CAMPUS_RANGE = (1, 2)
YEAR_RANGE = (1, 8)
QUARTER_RANGE = (1, 4)


def main():
    if not exists(DB_DIR):
        makedirs(DB_DIR, exist_ok=True)

    if not exists(join(DB_DIR, 'html')):
        makedirs(join(DB_DIR, 'html'), exist_ok=True)

    codes = generate_term_codes()
    print_c(f'Loaded {color(Fore.CYAN, len(codes))} term codes\n')

    print_c(f'Scraping session cookie…\r')

    cookies = scrape_cookies()
    print_c(f"Scraped session cookie {color(Fore.YELLOW, cookies['CPSESSID'])}\n{'-'*79}\n")

    temp_path = join(OLD_DB_DIR, 'temp.json')

    try:
        for term in codes:
            print_c(f" [{term}] [{color(Fore.YELLOW, 'MINING…')}] Scraping…\r")

            temp = TinyDB(temp_path)

            dept_data = mine_dept_data(term, write=False)
            print_c(f" [{term}] [{color(Fore.YELLOW, 'MINING…')}] \
                      Parsing {len(dept_data)} departments…\r")

            failed = False
            for idx, variant in enumerate(ADVANCED_FORM_DATA):
                content = mine_table_data(term, variant, dept_data, cookies, write=False)
                if advanced_parse(content, db=temp, term=term):
                    break
                elif idx == len(ADVANCED_FORM_DATA) - 1:
                    failed = True

            if rename(temp_path, join(OLD_DB_DIR, f'old_{term}_database.json')):
                remove(temp_path)

            db = TinyDB(join(OLD_DB_DIR, f'old_{term}_database.json'))

            num_courses = sum([len(db.table(t).all()) for t in db.tables()])

            if failed:
                print_c(f" [{term}] [{color(Fore.RED, 'ERROR!!')}] Payload failed…\n")
            else:
                print_c(f" [{term}] [{color(Fore.GREEN, 'SUCCESS')}] Mined {num_courses} courses\n")

    except KeyboardInterrupt:
        kill_driver()
        remove(temp_path)
    finally:
        kill_driver()


def mine_dept_data(term, write=False):
    '''
    Mine dept data will grab the department IDs for a given quarter.
    :param term: (str) the term to mine
    :param write: (bool) write to file?
    :return data (list(tuple)) the html body
    '''
    data = [('p_calling_proc', 'bwckschd.p_disp_dyn_sched'), ('p_term', f'{term}')]

    res = requests.post('https://banssb.fhda.edu/PROD/bwckgens.p_proc_term_date', data=data)
    res.raise_for_status()

    if write:
        write_to_file(res, term)

    soup = BeautifulSoup(res.content, "html5lib")
    select = soup.find('select', {'id': 'subj_id'})
    options = select.find_all('option')

    data = [('sel_subj', o['value']) for o in options]
    return data


def mine_table_data(term, payload, dept_data, cookies, write=False):
    '''
    Mine will hit the database for foothill's class listings
    :param term: (str) the term to mine
    :param payload: (str) data payload for request
    :param dept_data: (str) department data payload
    :param cookies: (dict) cookies to send with POST
    :param write: (bool) write to file?
    :return res.content: (json) the html body
    '''
    data = [('rsts', 'dummy'), ('crn', 'dummy'), ('term_in', f'{term}')]

    data.extend(payload[0])

    data.extend(dept_data)

    data.extend(payload[1])

    res = requests.post('https://banssb.fhda.edu/PROD/bwskfcls.P_GetCrse_Advanced',
                         cookies=cookies, data=data)
    res.raise_for_status()

    if write:
        write_to_file(res, term)

    return res.content


def advanced_parse(content, db, term=''):
    '''
    Advanced parse takes the content from the request and then populates the database with the data
    :param content: (html) The html containing the courses
    :param db: (TinyDB) the current database
    :return: None
    '''
    soup = BeautifulSoup(content, 'html5lib')

    try:
        table = soup.find('table', {'class': 'datadisplaytable'})
        table_rows = table.find_all('tr')

        table_headers = list()
        start_idx = 0
        for i, tr in enumerate(table_rows):
            header_cols = tr.find_all('th', {'class': 'ddheader'})
            for th in header_cols:
                table_headers.append(get_parsed_text(th))
            if table_headers:
                start_idx = i
                break

        for tr in table_rows[start_idx:]:
            try:
                cols = tr.find_all('td', {'class': 'dddefault'})

                if cols:
                    s = defaultdict(lambda: defaultdict(list))

                    num_blank = 0
                    for i, c in enumerate(cols):
                        a = c.find('a')
                        cols[i] = get_parsed_text(a) if a else get_parsed_text(cols[i])
                        if cols[i].isspace():
                            num_blank += 1

                    if num_blank > len(cols) - num_blank:
                        raise BlankRow

                    data = dict(zip(table_headers, cols))

                    subject = data['Subj']
                    key = data['Crse']
                    crn = data['CRN']

                    s[key][crn].append(data)

                    j = dict(s)
                    db.table(f'{subject}').insert(j)
            except BlankRow:
                continue
    except AttributeError as e:
        return False
    return True


def generate_term_codes():
    """
    This helper generates a list of term codes based on the ranges set by:
    YEAR_RANGE, QUARTER_RANGE, CAMPUS_RANGE
    :return: (list(str)) list of term codes
    """
    codes = []
    for i in range(YEAR_RANGE[0], YEAR_RANGE[1] + 1):
        for j in range(QUARTER_RANGE[0], QUARTER_RANGE[1] + 1):
            for k in range(CAMPUS_RANGE[0], CAMPUS_RANGE[1] + 1):
                codes.append(f'201{i}{j}{k}')
    return codes


class BlankRow(Exception):
    pass


def get_parsed_text(tag):
    """
    Regex that strips all html tags and their contents
    :param tag: (str) inner contents of parent tag
    :return: (str) isolated text
    """
    text = tag.get_text()
    p = re.compile(r'<.*?>')
    return p.sub('', text)


def print_c(message):
    """
    Clears last carriage returned line and writes a new one
    :param message: (str)
    :return: None
    """
    sys.stdout.write('\x1b[2K')
    sys.stdout.write(message)
    sys.stdout.flush()


def color(c, word):
    """
    Format template that inserts a color for a given word
    :param c: (Color) Color to format to
    :param word: (str) Word to format
    :return: (str) Formatted String
    """
    return f'{c}{word}{Style.RESET_ALL}'


def write_to_file(res, term):
    """
    Writes a bytestream to a nested file directory
    :param res: response object
    :param term: term code
    :return: None
    """
    with open(f"{join(DB_DIR, 'html', term+'.html')}", "wb") as file:
        for chunk in res.iter_content(chunk_size=512):
            if not chunk:
                break

            file.write(chunk)
            file.flush()


if __name__ == '__main__':
    init()
    main()
