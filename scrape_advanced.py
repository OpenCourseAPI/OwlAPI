import sys
from os import makedirs, rename, remove
from os.path import join, exists
from re import compile
from collections import defaultdict

from selenium_login import scrape_cookies, kill_driver
from settings import OLD_DB_DIR, SCHEDULE, ADVANCED_FORM_DATA

# 3rd party
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB

CAMPUS_RANGE = (1, 2)
YEAR_RANGE = (1, 8)
QUARTER_RANGE = (1, 4)


def main():
    if not exists(OLD_DB_DIR):
        makedirs(OLD_DB_DIR, exist_ok=True)

    codes = generate_term_codes()
    print(codes)

    cookies = scrape_cookies()
    print(cookies)

    temp_path = join(OLD_DB_DIR, 'temp.json')

    try:
        for term in codes:
            sys.stdout.write(f'[{term}] | Scraping…\r')
            sys.stdout.flush()

            temp = TinyDB(temp_path)

            dept_data = mine_dept_data(term, cookies, write=False)
            sys.stdout.write(f'[{term}] | Mining Depts… {[dept[1] for dept in dept_data]}\r')
            sys.stdout.flush()

            content = mine_table_data(term, dept_data, cookies, write=False)
            if not advanced_parse(content, db=temp, term=term):
                continue

            rename(temp_path, join(OLD_DB_DIR, f'old_{term}_database.json'))

            db = TinyDB(join(OLD_DB_DIR, f'old_{term}_database.json'))
            print(f'[{term}] | ', db.tables())

    except KeyboardInterrupt:
        kill_driver()
        remove(temp_path)
    finally:
        kill_driver()


def mine_dept_data(term, cookies, write=False):
    import requests

    data = [('p_calling_proc', 'bwckschd.p_disp_dyn_sched'), ('p_term', f'{term}')]

    res = requests.post('https://banssb.fhda.edu/PROD/bwckgens.p_proc_term_date', data=data)
    res.raise_for_status()

    if write:
        with open(f'{join(OLD_DB_DIR, SCHEDULE)}', "wb") as file:
            for chunk in res.iter_content(chunk_size=512):
                if not chunk:
                    break

                file.write(chunk)
                file.flush()

    soup = BeautifulSoup(res.content, "html5lib")
    select = soup.find('select', {'id': 'subj_id'})
    options = select.find_all('option')

    data = [('sel_subj', o['value']) for o in options]
    return data


def mine_table_data(term, dept_data, cookies, write=False):
    '''
    Mine will hit the database for foothill's class listings
    :param term: (str) the term to mine
    :param cookies: (dict) cookies to send with POST
    :param write: (bool) write to file?
    :return res.content: (json) the html body
    '''

    data = [('rsts', 'dummy'), ('crn', 'dummy'), ('term_in', f'{term}'), ('sel_subj', 'dummy')]

    data.extend(dept_data)

    data.extend(ADVANCED_FORM_DATA)

    res = requests.post('https://banssb.fhda.edu/PROD/bwskfcls.P_GetCrse_Advanced', cookies=cookies, data=data)
    res.raise_for_status()

    if write:
        with open(f'{join(OLD_DB_DIR, SCHEDULE)}', "wb") as file:
            for chunk in res.iter_content(chunk_size=512):
                if not chunk:
                    break

                file.write(chunk)
                file.flush()

    return res.content


class BlankRow(Exception):
    pass


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

                if len(cols) > 0:
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
        print(f'[{term}] | ERROR: {e}')
        return False
    return True


def generate_term_codes():
    codes = []
    for i in range(YEAR_RANGE[0], YEAR_RANGE[1] + 1):
        for j in range(QUARTER_RANGE[0], QUARTER_RANGE[1] + 1):
            for k in range(CAMPUS_RANGE[0], CAMPUS_RANGE[1] + 1):
                codes.append(f'201{i}{j}{k}')
    return codes


def get_parsed_text(tag):
    text = tag.get_text()
    p = compile(r'<.*?>')
    return p.sub('', text)


if __name__ == '__main__':
    main()
