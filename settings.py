import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(ROOT_DIR, 'db')

DAYS_PATTERN = f"^{'(M|T|W|Th|F|S|U)?'*7}$"

HEADERS = ('course', 'CRN', 'desc', 'status', 'days', 'time', 'start', 'end', 'room', 'campus', 'units', 'instructor', 'seats', 'wait_seats', 'wait_cap')

SSB_URL = 'https://ssb-prod.ec.fhda.edu'

'''
Campus - Foothill, De Anza, and `test`
'''
CAMPUS_LIST = {'fh': '202121', 'da': '202122', 'test': 'test'}

'''
Course Type Flags - Foothill College

Online   - online, fully asynchronous classes (no live meetings)
Virtual  - online, fully synchronous classes (only live meetings)
Hybrid   - online, hybrid (mixed) between `online` and `virtual` [COVID-19]
Standard - physical classes (or all of the above are N/A, e.g. "Independent Study")
'''
FH_TYPE_ALIAS = {'standard': None, 'online': 'W', 'virtual': 'V', 'hybrid': 'Z'}

'''
Course Type Flags - De Anza College

Online   - online, fully asynchronous classes (no live meetings)
Hybrid   - hybrid classes that are both online and physical
Standard - physical classes (or all of the above are N/A, e.g. "Independent Study")
'''
DA_TYPE_ALIAS = {'standard': None, 'online': 'Z', 'hybrid': 'Y'}

COURSE_TYPES_TO_FLAGS = {
    'fh': FH_TYPE_ALIAS,
    'da': DA_TYPE_ALIAS,
    'test': FH_TYPE_ALIAS
}
