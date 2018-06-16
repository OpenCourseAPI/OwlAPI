import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(ROOT_DIR, 'db')
TEST_DIR = os.path.join(ROOT_DIR, 'tests')
TEST_DB_DIR = os.path.join(TEST_DIR, 'test_db')

COURSE_PATTERN = r'[FD]0*(\d*\w?)\.?\d*([YWZH])?'
DAYS_PATTERN = f"^{'(M|T|W|Th|F|S|U)?'*7}$"


SCHEDULE = 'schedule.html'
HEADERS = ('course', 'CRN', 'desc', 'status', 'days', 'time', 'start', 'end', 'room', 'campus', 'units', 'instructor', 'seats', 'wait_seats', 'wait_cap')

CAMPUS_LIST = {'fh': '201911', 'da': '201912', 'test': 'test'}
