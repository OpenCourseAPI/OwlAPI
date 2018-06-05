from collections import defaultdict
from os import makedirs, rename, remove
from os.path import join, exists

from scrape_term import get_key
from settings import DB_DIR, ADVANCED_HEADERS, PAST_TERM_CODES, SCHEDULE

# 3rd party
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB

def main():
    if not exists(DB_DIR):
        makedirs(DB_DIR, exist_ok=True)

    for term in PAST_TERM_CODES.values():
        temp_path = join(DB_DIR, 'temp.json')
        temp = TinyDB(temp_path)

        content = mine(term, write=True)
        advanced_parse(content, db=temp)

        if rename(temp_path, join(DB_DIR, f'old_{term}_database.json')):
            remove(temp_path)

        db = TinyDB(join(DB_DIR, f'old_{term}_database.json'))
        print(term, db.tables())

def mine(term, write=False):
    '''
    Mine will hit the database for foothill's class listings
    :param term: (str) the term to mine
    :param write: (bool) write to file?
    :return res.content: (json) the html body
    '''
    cookies = {
        'TESTID': 'SET',
        'badprotocol': '3',
        'shib_idp_session': 'ad53da4cf9b9a4c1f354e513c10c60802592d842df45e292e94acb39e4f22f3c',
        'BANSSO': 'F1538D4DA70C773174EDA34DF454DCA1E95FBB970A1B3C78D794E9F6850F167B',
        'fos.web.server': 'lumweb3',
        'fos.secure.web.server': 'lumweb3',
        'runId': '-5887403237976173719',
        'usid': 'nEekhNSMntHK2/GY/bTtOA__',
        'CPSESSID': 'AQARMjAxODA2MDUwMTE4MjUDABA1NlBKWTcxODI5MzAz',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'https://banssb.fhda.edu',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3202.29 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://banssb.fhda.edu/PROD/bwskfcls.P_GetCrse',
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

    res = requests.post('https://banssb.fhda.edu/PROD/bwskfcls.P_GetCrse_Advanced', headers=headers, cookies=cookies, data=data)
    res.raise_for_status()

    if write:
        with open(f'{join(DB_DIR, SCHEDULE)}', "wb") as file:
            for chunk in res.iter_content(chunk_size=512):
                if chunk:
                    file.write(chunk)

    return res.content


def advanced_parse(content, db):
    '''
    Advanced parse takes the content from the request and then populates the database with the data
    :param content: (html) The html containing the courses
    :param db: (TinyDB) the current database
    :return: None
    '''
    soup = BeautifulSoup(content, 'html5lib')

    table = soup.find('table', {'class': 'datadisplaytable'})
    table_rows = table.find_all('tr')
    for tr in table_rows[:5]:
        td = tr.find_all('td', {'class': 'dddefault'})
        print(td)


def parse(content, db):
    '''
    Parse takes the content from the request and then populates the database with the data
    :param content: (html) The html containing the courses
    :param db: (TinyDB) the current database
    '''
    soup = BeautifulSoup(content, 'html5lib')

    tables = soup.find_all('table', {'class': 'TblCourses'})
    for t in tables:
        dept = t['dept'].replace(' ', '')
        dept_desc = t['dept-desc']

        rows = t.find_all('tr', {'class': 'CourseRow'})
        s = defaultdict(lambda: defaultdict(list))
        for r in rows:
            cols = r.find_all(lambda tag: tag.name == 'td' and not tag.get_text().isspace())

            if cols:
                for i, c in enumerate(cols):
                    a = c.find('a')
                    cols[i] = a.get_text() if a else cols[i].get_text()

                try:
                    key = get_key(f'{cols[0] if cols[0] else cols[1]}')[0]
                    data = dict(zip(ADVANCED_HEADERS, cols))

                    crn = data['CRN']
                    if s[key][crn]:
                        comb = set(s[key][crn][0].items()) ^ set(data.items())
                        if not comb:
                            continue

                    data['units'] = data['units'].lstrip()

                    s[key][crn].append(data)
                except KeyError:
                    continue

        j = dict(s)
        db.table(f'{dept}').insert(j)


if __name__ == '__main__':
    main()
