from os.path import join

from unittest import TestCase, skip
from tinydb import TinyDB

from server import generate_url, get_one

import test.test_db.data as test_data
from settings import TEST_DIR

test_database = TinyDB(join(TEST_DIR, 'test_db', 'fh_database.json'))


class TestGenerateURL(TestCase):
    def test_sample_url_can_be_generated(self):
        self.assertEqual(
            test_data.test_sample_url_can_be_generated_data,
            generate_url('test_dept', 'test_course')
        )


class TestGetOne(TestCase):
    @skip("too large")
    def test_get_one_dept(self):
        data = {'dept': 'CS'} # floof.li/single?dept=CS

        result = get_one(db=test_database, data=data, filters=dict())
        self.assertEqual(
            test_data.test_get_one_dept_data,
            result
        )

    def test_get_one_dept_returns_right_n_courses(self):
        data = {'dept': 'CS'}

        result = get_one(db=test_database, data=data, filters=dict())
        self.assertEqual(
            len(test_data.test_get_one_dept_data[0]),
            len(result[0])
        )

    def test_get_one_dept_and_course(self):
        data = {'dept': 'CS', 'course': '2A'}

        result = get_one(db=test_database, data=data, filters=dict())
        self.assertEqual(
            test_data.test_get_one_dept_and_course_data,
            result
        )
