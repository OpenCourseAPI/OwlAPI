from os import remove
from os.path import join
from filecmp import cmp

from unittest import TestCase
from tinydb import TinyDB

from scrape_term import parse
from settings import DB_DIR
from .generate_test_db import SCHEDULE, TEST_DB

class TestScrapeTerm(TestCase):
    def test_data_matches(self):
        with open(join(DB_DIR, SCHEDULE), "r") as file:
            temp_path = join(DB_DIR, 'temp_test_database.json')
            temp = TinyDB(temp_path)
            temp.drop_tables()

            content = file.read()
            parse(content, db=temp)

            self.assertTrue(cmp(temp_path, join(DB_DIR, TEST_DB)),
                            'Generated Test DBs do not match')

            remove(temp_path)
