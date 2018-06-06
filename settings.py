import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(ROOT_DIR, 'db')
OLD_DB_DIR = os.path.join(DB_DIR, 'old')
TEST_DIR = os.path.join(ROOT_DIR, 'tests')
TEST_DB_DIR = os.path.join(TEST_DIR, 'test_db')

COURSE_PATTERN = r'[FD]0*(\d*\w?)\.?\d*([YWZH])?'
DAYS_PATTERN = f"^{'(M|T|W|Th|F|S|U)?'*7}$"

SCHEDULE = 'schedule.html'
HEADERS = ('course', 'CRN', 'desc', 'status', 'days', 'time', 'start', 'end',
           'room', 'campus', 'units', 'instructor', 'seats', 'wait_seats', 'wait_cap')
CURRENT_TERM_CODES = CAMPUS_LIST = {'fh': '201911', 'da': '201912', 'test': 'test'}

ADVANCED_HEADERS = ('select', 'CRN', 'subject', 'section', 'course', 'campus', 'units', 'title', 'days', 'time',
                    'seats_cap', 'seats_act', 'seats', 'wait_cap', 'wait_act', 'wait_seats', 'instructor',
                    'date_range', 'location')
PAST_TERM_CODES = {'fh': '201831'}
