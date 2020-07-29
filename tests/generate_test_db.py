'''
Usage: python3 -m tests.generate_test_db [--fetch]

More Info: python3 -m tests.generate_test_db --help
'''

from os import makedirs, rename, remove
from os.path import join, exists
from argparse import ArgumentParser

# 3rd party
from tinydb import TinyDB

from scrape_term import mine, parse
from settings import DB_DIR

TERM_CODE = '202121' # Foothill, Fall 2020
SCHEDULE = 'test_schedule.html'
TEST_DB = join(DB_DIR, 'test_database.json')


def fetch():
    '''
    Download and save raw HTML for a term as a file
    '''
    mine(TERM_CODE, join(DB_DIR, SCHEDULE))


def generate():
    '''
    Generate a test database from the fetched HTML
    '''
    if not exists(DB_DIR):
        makedirs(DB_DIR, exist_ok=True)

    with open(f'{join(DB_DIR, SCHEDULE)}', "r") as file:
        temp_path = join(DB_DIR, 'temp.json')
        temp = TinyDB(temp_path)

        content = file.read()
        parse(content, db=temp)

        if rename(temp_path, TEST_DB):
            remove(temp_path)

        db = TinyDB(TEST_DB)
        print('Departments:', ', '.join(list(db.tables())))


if __name__ == "__main__":
    parser = ArgumentParser(description='Fetch and generate test databases')
    parser.add_argument('--fetch', action='store_true',
                        help='update the HTML file `db/test_schedule.html`')
    args = parser.parse_args()

    if args.fetch:
        print('Fetching HTML file...')
        fetch()
        print('HTML file fetched\n')

    print('Generating test database...')
    generate()
    print('Test DB generated')
