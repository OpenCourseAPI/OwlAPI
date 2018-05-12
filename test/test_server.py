from os.path import join

from unittest import TestCase, skip
from tinydb import TinyDB

from server import generate_url, get_one, get_many

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
    def test_get_one_dept(self):
        data = {'dept': 'CS'}  # floof.li/single?dept=CS

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


class TestGetMany(TestCase):
    def test_get_many_dept(self):
        data = {'courses': [{'dept': 'CS'}, {'dept': 'MATH'}]}

        result = get_many(db=test_database, data=data['courses'], filters=dict())
        self.assertEqual(
            test_data.test_get_two_dept_data,
            result
        )

    def test_get_many_dept_returns_right_n_courses(self):
        data = {'courses': [{'dept': 'CS'}, {'dept': 'MATH'}]}

        result = get_many(db=test_database, data=data['courses'], filters=dict())
        self.assertEqual(
            len(test_data.test_get_two_dept_data[0]),
            len(result[0])
        )