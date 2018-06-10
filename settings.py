import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(ROOT_DIR, 'db')
OLD_DB_DIR = os.path.join(DB_DIR, 'old')
TEST_DIR = os.path.join(ROOT_DIR, 'tests')
TEST_DB_DIR = os.path.join(TEST_DIR, 'test_db')

COURSE_PATTERN = r'[FD]0*(\d*\w?)\.?\d*([YWZH])?'
DAYS_PATTERN = f"^{'(M|T|W|Th|F|S|U)?'*7}$"

SCHEDULE = 'schedule.html'
SEARCH = 'search.html'
HEADERS = ('course', 'CRN', 'desc', 'status', 'days', 'time', 'start', 'end',
           'room', 'campus', 'units', 'instructor', 'seats', 'wait_seats', 'wait_cap')
CURRENT_TERM_CODES = CAMPUS_LIST = {'fh': '201911', 'da': '201912', 'test': 'test'}

ADVANCED_FORM_DATA = [
    [
        [('sel_subj', 'dummy'),
         ('sel_day', 'dummy'),
         ('sel_schd', 'dummy'),
         ('sel_insm', 'dummy'),
         ('sel_camp', 'dummy'),
         ('sel_levl', 'dummy'),
         ('sel_sess', 'dummy'),
         ('sel_instr', 'dummy'),
         ('sel_ptrm', 'dummy'),
         ('sel_attr', 'dummy')],
        [('sel_crse', ''),
         ('sel_title', ''),
         ('sel_from_cred', ''),
         ('sel_to_cred', ''),
         ('sel_camp', '%'),
         ('sel_sess', '%'),
         ('sel_instr', '%'),
         ('sel_ptrm', '%'),
         ('begin_hh', '0'),
         ('begin_mi', '0'),
         ('begin_ap', 'a'),
         ('end_hh', '0'),
         ('end_mi', '0'),
         ('end_ap', 'a'),
         ('SUB_BTN', 'Section Search'),
         ('path', '1')]
    ],

    [
        [('sel_subj', 'dummy'),
         ('sel_day', 'dummy'),
         ('sel_schd', 'dummy'),
         ('sel_insm', 'dummy'),
         ('sel_camp', 'dummy'),
         ('sel_levl', 'dummy'),
         ('sel_sess', 'dummy'),
         ('sel_instr', 'dummy'),
         ('sel_ptrm', 'dummy'),
         ('sel_attr', 'dummy')],
        [('sel_crse', ''),
         ('sel_title', ''),
         ('sel_schd', '%'),
         ('sel_from_cred', ''),
         ('sel_to_cred', ''),
         ('sel_camp', '%'),
         ('sel_instr', '%'),
         ('sel_sess', '%'),
         ('sel_ptrm', '%'),
         ('sel_attr', '%'),
         ('begin_hh', '0'),
         ('begin_mi', '0'),
         ('begin_ap', 'a'),
         ('end_hh', '0'),
         ('end_mi', '0'),
         ('end_ap', 'a'),
         ('SUB_BTN', 'Section Search'),
         ('path', '1')]
    ]
]
