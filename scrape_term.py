from os import makedirs, rename, remove
from os.path import join, exists
from re import match
from collections import defaultdict

# 3rd party
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB

from settings import DB_DIR, COURSE_PATTERN, HEADERS, SCHEDULE

CURRENT_TERM_CODES = {'fh': '202111', 'da': '201912'}


def main():
    if not exists(DB_DIR):
        makedirs(DB_DIR, exist_ok=True)

    for term in CURRENT_TERM_CODES.values():
        temp_path = join(DB_DIR, 'temp.json')
        temp = TinyDB(temp_path)

        content = mine(term)
        parse(content, db=temp)

        if rename(temp_path, join(DB_DIR, f'{term}_database.json')):
            remove(temp_path)

        db = TinyDB(join(DB_DIR, f'{term}_database.json'))
        print(term, db.tables())


def mine(term, write=False):
    '''
    Mine will hit the database for foothill's class listings
    :param term: (str) the term to mine
    :param write: (bool) write to file?
    :return res.content: (json) the html body
    '''
    data = [('termcode', f'{term}')]

    res = requests.post('https://ssb-prod.ec.fhda.edu/PROD/fhda_opencourses.P_GetCourseList', data=data)
    res.raise_for_status()

    if write:
        with open(f'{join(DB_DIR, SCHEDULE)}', "wb") as file:
            for chunk in res.iter_content(chunk_size=512):
                if chunk:
                    file.write(chunk)

    return res.content


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
        for tr in rows:
            cols = tr.find_all(lambda tag: tag.name == 'td' and not tag.get_text().isspace())

            if cols:
                for i, c in enumerate(cols):
                    a = c.find('a')
                    cols[i] = a.get_text() if a else cols[i].get_text()

                try:
                    key = get_key(f'{cols[0] if cols[0] else cols[1]}')[0]
                    data = dict(zip(HEADERS, cols))

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


def get_key(course):
    '''
    This is the key parser for the course names
    :param course: (str) The unparsed string containing the course name
    :return match_obj.groups(): (list) the string for the regex match
    '''
    c = course.split(' ')
    idx = 1 if len(c) < 3 else 2
    section = c[idx]

    match_obj = match(COURSE_PATTERN, section)
    return match_obj.groups()


if __name__ == "__main__":
    main()
