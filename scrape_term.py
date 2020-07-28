from os import makedirs, rename, remove
from os.path import join, exists
from collections import defaultdict

# 3rd party
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB
from marshmallow import ValidationError as MarshValidationError

from owl_models import InterimClassDataSchema, ClassDataSchema, ClassTimeSchema
from utils import parse_course_str, ValidationError, log_info, log_err
from settings import DB_DIR, SSB_URL, HEADERS

CURRENT_TERM_CODES = {'fh': '202121', 'da': '202122'}

classDataSchema = ClassDataSchema()
classTimeSchema = ClassTimeSchema()
interimClassDataSchema = InterimClassDataSchema()


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

        depts = ', '.join(db.tables())
        log_info(f'Scraped term {term}', pad=False, details={
            'depts': depts,
        })


def mine(term, filename=None):
    '''
    Mine will hit the database for foothill's class listings
    :param term: (str) the term to mine
    :param filename: (str) file to write html to
    :return res.content: (json) the html body
    '''
    data = [('termcode', f'{term}')]

    res = requests.post(SSB_URL + '/PROD/fhda_opencourses.P_GetCourseList', data=data)
    res.raise_for_status()

    if filename:
        with open(f'{join(DB_DIR, filename)}', "wb") as file:
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
        # TODO: verify whether replacing spaces yields correct dept names in all scenarios
        dept = t['dept'].replace(' ', '')
        dept_desc = t['dept-desc']

        rows = t.find_all('tr', {'class': 'CourseRow'})
        s = defaultdict(lambda: defaultdict(list))
        for tr in rows:
            cols = tr.find_all(lambda tag: tag.name == 'td')

            if cols:
                # The first <td> is a field that is not relevant to us
                # it is either empty or contains a "flag" icon
                cols.pop(0)

                for i, c in enumerate(cols):
                    a = c.find('a')
                    cols[i] = (a.get_text() if a else cols[i].get_text()).strip()

                try:
                    parsed_course = parse_course_str(cols[0])
                    key = parsed_course['course']
                    data = dict(zip(HEADERS, cols))

                    if parsed_course['dept'] != dept:
                        raise ValidationError(
                            'Departments do not match',
                            f"'{parsed_course['dept']}' != '{dept}'"
                        )

                    data['units'] = data['units'].lstrip()
                    data['dept'] = dept
                    data['section'] = parsed_course['section']

                    try:
                        data = interimClassDataSchema.load(data)
                    except MarshValidationError as e:
                        print(e.messages, data)
                        continue

                    crn = data['CRN']
                    if s[key][crn]:
                        comb = set(s[key][crn][0].items()) ^ set(data.items())
                        if not comb:
                            continue

                    s[key][crn].append(data)
                except KeyError:
                    continue
                except ValidationError as e:
                    log_err('Unable to parse course - data validation failed', details={
                        'message': e.message,
                        'details': e.details,
                        'course': cols,
                    })
                    print('\n')
                    continue

        j = defaultdict(defaultdict)

        for course, section in s.items():
            for cl in section.values():
                data = classDataSchema.load(cl[0])
                classTime = [classTimeSchema.load(c) for c in cl]

                check_integrity(cl, data, classTime)

                data['time'] = classTime
                j[course][data['CRN']] = data

        db.table(f'{dept}').insert(dict(j))


def check_integrity(cl, data, times):
    dataSets = [set(classDataSchema.load(c).items()) for c in cl]
    timeSets = [set(t.items()) for t in times]

    if len(cl) > 1:
        for i in range(len(cl) - 1):
            comb = dataSets[i] ^ dataSets[i + 1]
            timeComb = timeSets[i] ^ timeSets[i + 1]

            if comb:
                print(data['CRN'], len(dataSets), comb)

            # if not timeComb:
            #     print(data['CRN'], timeComb, comb)


if __name__ == "__main__":
    main()
