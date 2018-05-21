from os.path import join

from unittest import TestCase, skip
from tinydb import TinyDB

from server import generate_url, get_one, get_many, filter_courses

from .test_db import data as test_data
from settings import TEST_DIR

test_database = TinyDB(join(TEST_DIR, 'test_db', 'test_database.json'))


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

    def test_get_one_dept_returns_n_courses(self):
        data = {'dept': 'CS'}

        result = get_one(db=test_database, data=data, filters=dict())
        self.assertEqual(
            len(test_data.test_get_one_dept_data[0].keys()),
            len(result[0].keys())
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

    def test_get_many_dept_returns_n_courses(self):
        data = {'courses': [{'dept': 'CS'}, {'dept': 'MATH'}]}

        result = get_many(db=test_database, data=data['courses'], filters=dict())
        self.assertEqual(
            len(test_data.test_get_two_dept_data[0]),
            len(result[0])
        )

class TestFilters(TestCase):
    def test_filters_status_returns_n_courses(self):
        data = {'courses': [{'dept':'CS', 'course':'1A'}], 'filters': {'status': {'open':0, 'waitlist':1, 'full':0}}}

        result = get_many(db=test_database, data=data['courses'], filters=data['filters'])

        self.assertEqual(
            1,
            len(result[0].keys())
        )

    def test_filters_type_returns_n_courses(self):
        data = {'courses':[{'dept':'CS','course':'1A'}], 'filters':{'types':{'standard':0, 'online':1, 'hybrid':0}}}

        result = get_many(db=test_database, data=data['courses'], filters=data['filters'])

        self.assertEqual(
            4,
            len(result[0].keys())
        )

    def test_filters_days_returns_n_courses(self):
        data = {'courses':[{'dept':'DANC','course':'14'}], 'filters':{'days':{'M':1, 'T':0, 'W':0, 'Th':0, 'F':0, 'S':0, 'U':0}}}

        result = get_many(db=test_database, data=data['courses'], filters=data['filters'])

        self.assertEqual(
            1,
            len(result[0].keys())
        )

    def test_filters_time_returns_n_courses(self):
        data = {'courses':[{'dept':'DANC','course':'14'}], 'filters': {'time':{'start':'7:30 AM', 'end':'12:00 PM'}}}

        result = get_many(db=test_database, data=data['courses'], filters=data['filters'])

        self.assertEqual(
            1,
            len(result[0].keys())
        )
