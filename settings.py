import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(ROOT_DIR, 'db')

COURSE_PATTERN = r'[FD]0*(\d*\w?)\.?\d*([YWZH])?'
DAYS_PATTERN = f"^{'(M|T|W|Th|F|S|U)?'*7}$"

HEADERS = ('course', 'CRN', 'desc', 'status', 'days', 'time', 'start', 'end', 'room', 'campus', 'units', 'instructor', 'seats', 'wait_seats', 'wait_cap')

CAMPUS_LIST = {'fh': '202121', 'da': '202122', 'test': 'test'}

SSB_URL = 'https://ssb-prod.ec.fhda.edu'
