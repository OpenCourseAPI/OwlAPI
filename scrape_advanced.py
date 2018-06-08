import sys
from os import makedirs, rename, remove
from os.path import join, exists
from re import compile
from collections import defaultdict

from selenium_login import scrape_cookies, kill_driver
from settings import OLD_DB_DIR, SCHEDULE

# 3rd party
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB

CAMPUS_RANGE = (1, 2)
YEAR_RANGE = (0, 8)
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

            content = mine(term, cookies, write=False)
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


def mine(term, cookies, write=False):
    '''
    Mine will hit the database for foothill's class listings
    :param term: (str) the term to mine
    :param cookies: (dict) cookies to send with POST
    :param write: (bool) write to file?
    :return res.content: (json) the html body
    '''

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'https://banssb.fhda.edu',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://banssb.fhda.edu/PROD/bwskfcls.P_GetCrse_Advanced',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,la;q=0.8',
        'DNT': '1',
    }

    data = [
      ('rsts', 'dummy'),
      ('crn', 'dummy'),
      ('term_in', f'{term}'),
      ('sel_subj', 'dummy'),
      ('sel_subj', 'ACTG'),
      ('sel_subj', 'ALCB'),
      ('sel_subj', 'ALTW'),
      ('sel_subj', 'AHS'),
      ('sel_subj', 'ANTH'),
      ('sel_subj', 'APSM'),
      ('sel_subj', 'ART'),
      ('sel_subj', 'ASTR'),
      ('sel_subj', 'ATHL'),
      ('sel_subj', 'BIOL'),
      ('sel_subj', 'BUSI'),
      ('sel_subj', 'CRLP'),
      ('sel_subj', 'CHEM'),
      ('sel_subj', 'CHLD'),
      ('sel_subj', 'COMM'),
      ('sel_subj', 'C S'),
      ('sel_subj', 'CNSL'),
      ('sel_subj', 'CRWR'),
      ('sel_subj', 'DANC'),
      ('sel_subj', 'D A'),
      ('sel_subj', 'D H'),
      ('sel_subj', 'DMS'),
      ('sel_subj', 'ECON'),
      ('sel_subj', 'EMS'),
      ('sel_subj', 'ENGR'),
      ('sel_subj', 'ENGL'),
      ('sel_subj', 'ESLL'),
      ('sel_subj', 'HORT'),
      ('sel_subj', 'JFS'),
      ('sel_subj', 'GEOG'),
      ('sel_subj', 'GIST'),
      ('sel_subj', 'GID'),
      ('sel_subj', 'HLTH'),
      ('sel_subj', 'HIST'),
      ('sel_subj', 'HUMN'),
      ('sel_subj', 'ITRN'),
      ('sel_subj', 'JAPN'),
      ('sel_subj', 'KINS'),
      ('sel_subj', 'L A'),
      ('sel_subj', 'LINC'),
      ('sel_subj', 'LIBR'),
      ('sel_subj', 'MATH'),
      ('sel_subj', 'MDIA'),
      ('sel_subj', 'MTEC'),
      ('sel_subj', 'MUS'),
      ('sel_subj', 'NCBS'),
      ('sel_subj', 'NCBH'),
      ('sel_subj', 'NCEL'),
      ('sel_subj', 'NCLA'),
      ('sel_subj', 'NCP'),
      ('sel_subj', 'NCSV'),
      ('sel_subj', 'P A'),
      ('sel_subj', 'PHT'),
      ('sel_subj', 'PHIL'),
      ('sel_subj', 'PHOT'),
      ('sel_subj', 'PHED'),
      ('sel_subj', 'PHDA'),
      ('sel_subj', 'PSE'),
      ('sel_subj', 'PHYS'),
      ('sel_subj', 'POLI'),
      ('sel_subj', 'PCA'),
      ('sel_subj', 'PSYC'),
      ('sel_subj', 'R T'),
      ('sel_subj', 'RSPT'),
      ('sel_subj', 'SOSC'),
      ('sel_subj', 'SOC'),
      ('sel_subj', 'SPAN'),
      ('sel_subj', 'THTR'),
      ('sel_subj', 'V T'),
      ('sel_subj', 'VITI'),
      ('sel_subj', 'WMN'),
      ('sel_day', 'dummy'),
      ('sel_schd', 'dummy'),
      ('sel_insm', 'dummy'),
      ('sel_camp', 'dummy'),
      ('sel_camp', '%'),
      ('sel_levl', 'dummy'),
      ('sel_sess', 'dummy'),
      ('sel_sess', '%'),
      ('sel_instr', 'dummy'),
      ('sel_instr', '%'),
      ('sel_ptrm', 'dummy'),
      ('sel_ptrm', '%'),
      ('sel_attr', 'dummy'),
      ('sel_crse', ''),
      ('sel_title', ''),
      ('sel_from_cred', ''),
      ('sel_to_cred', ''),
      ('begin_hh', '0'),
      ('begin_mi', '0'),
      ('begin_ap', 'a'),
      ('end_hh', '0'),
      ('end_mi', '0'),
      ('end_ap', 'a'),
      ('SUB_BTN', 'Section Search'),
      ('path', '1'),
    ]

    res = requests.post('https://banssb.fhda.edu/PROD/bwskfcls.P_GetCrse_Advanced',
                        headers=headers, cookies=cookies, data=data)
    res.raise_for_status()

    if write:
        with open(f'{join(DB_DIR, SCHEDULE)}', "wb") as file:
            for chunk in res.iter_content(chunk_size=512):
                if chunk:
                    file.write(chunk)

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
