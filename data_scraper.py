from urllib.request import urlopen
from os import makedirs
from os.path import abspath, join, exists
from collections import defaultdict
from json import dumps
from re import match

# 3rd party
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB

SCHEDULE = 'schedule.html'
TERM_CODE = '201841'
HEADERS = ('course', 'CRN', 'desc', 'status', 'days', 'time', 'start', 'end',
           'room', 'campus', 'units', 'instructor', 'seats', 'wait_seats', 'wait_cap')
DB_ROOT = 'db/'

def main():
    if not exists(DB_ROOT):
        makedirs(DB_ROOT, exist_ok=True)

    content = urlopen(f'file://{abspath(SCHEDULE)}') if exists(SCHEDULE) else mine()
    db = TinyDB(join(DB_ROOT, 'database.json'))

    parse(content, db=db)
    print(db.tables())


def mine(write=True):
    '''
    Mine will hit the database for foothill's class listings and write it to a file.
    :param write: (bool) write to file?
    :return res.content: (json) the html body
    '''
    headers = {
        'Origin': 'https://banssb.fhda.edu',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'FoothillAPI',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html, */*; q=0.01',
        'Referer': 'https://banssb.fhda.edu/PROD/fhda_opencourses.P_Application',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = [('termcode', f'{TERM_CODE}'), ]

    res = requests.post('https://banssb.fhda.edu/PROD/fhda_opencourses.P_GetCourseList', headers=headers, data=data)
    res.raise_for_status()

    if write:
        with open(f'{SCHEDULE}', "wb") as file:
            for chunk in res.iter_content(chunk_size=512):
                if chunk:
                    file.write(chunk)

    return res.content


def parse(content, db):
    db.purge_tables()
    soup = BeautifulSoup(content, 'html5lib')

    tables = soup.find_all('table', {'class': 'TblCourses'})
    for t in tables:
        dept = t['dept'].replace(' ', '')
        dept_desc = t['dept-desc']

        rows = t.find_all('tr', {'class': 'CourseRow'})
        s = defaultdict(lambda: defaultdict(list))  # key: list()
        for r in rows:
            cols = r.find_all(lambda tag: tag.name == 'td' and not tag.get_text().isspace())

            if cols:
                for i, c in enumerate(cols):
                    a = c.find('a')
                    cols[i] = a.get_text() if a else cols[i].get_text()

                try:
                    key = get_key(f'{cols[0]}')[0]
                    data = dict(zip(HEADERS, cols))
                    crn = data['CRN']

                    if len(s[key][crn]) > 0:
                        comb = set(s[key][crn][0].items()) ^ set(data.items())
                        if len(comb) == 0:
                            continue
                    s[key][crn].append(data)
                except KeyError:
                    continue

        j = dict(s)
        db.table(f'{dept}').insert(j)


def get_key(course):
    c = course.split(' ')
    idx = 1 if len(c) < 3 else 2
    section = c[idx]

    match_obj = match('F0*(\d*\w?)\.?\d*([YWH])?', section)
    return match_obj.groups()


if __name__ == "__main__":
    main()
