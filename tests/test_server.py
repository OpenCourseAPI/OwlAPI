from os.path import join

import pytest
from snapshottest import TestCase
from tinydb import TinyDB

import settings
from server import generate_url, get_one, get_many


test_database = TinyDB(join(settings.DB_DIR, 'test_database.json'))


@pytest.mark.usefixtures('fix_snapshots')
class TestGenerateURL(TestCase):
    def test_sample_url_can_be_generated(self):
        self.assertEqual(
            {'dept': 'test_dept', 'course': 'test_course'},
            generate_url('test_dept', 'test_course')
        )


@pytest.mark.usefixtures('fix_snapshots')
class TestGetOne(TestCase):
    def test_get_one_dept(self):
        data = {'dept': 'CS'}  # opencourse.dev/<campus>/single?dept=CS

        result = get_one(campus='test', db=test_database, data=data, filters=dict())
        self.assertMatchSnapshot(result)


    def test_get_one_dept_and_course(self):
        data = {'dept': 'CS', 'course': '2A'}

        result = get_one(campus='test', db=test_database, data=data, filters=dict())
        self.assertMatchSnapshot(result)

    def test_get_one_dept_and_honors_course(self):
        data = {'dept': 'MUS', 'course': '2AH'}

        result = get_one(campus='test', db=test_database, data=data, filters=dict())
        self.assertMatchSnapshot(result)


@pytest.mark.usefixtures('fix_snapshots')
class TestGetMany(TestCase):
    def test_get_many_dept(self):
        data = {'courses': [{'dept': 'CS'}, {'dept': 'MATH'}]}

        result = get_many(campus='test', db=test_database, data=data['courses'], filters=dict())
        self.assertMatchSnapshot(result)


@pytest.mark.usefixtures('fix_snapshots')
class TestFilters(TestCase):
    def test_filters_status_returns_n_courses(self):
        data = {'courses': [{'dept':'CS', 'course':'1A'}],
                'filters': {'status': {'open':0, 'waitlist':1, 'full':0}}}

        result = get_many(campus='test', db=test_database, data=data['courses'], filters=data['filters'])

        self.assertEqual(
            1,
            len(result[0].keys())
        )

    def test_filters_type_returns_n_courses(self):
        data = {'courses':[{'dept':'CS', 'course':'1A'}],
                'filters':{'types':{'standard':0, 'online':1, 'hybrid':0}}}

        result = get_many(campus='test', db=test_database, data=data['courses'], filters=data['filters'])

        self.assertEqual(
            4,
            len(result[0].keys())
        )

    def test_filters_days_returns_n_courses(self):
        data = {'courses':[{'dept':'DANC', 'course':'14'}],
                'filters':{'days':{'M':1, 'T':0, 'W':0, 'Th':0, 'F':0, 'S':0, 'U':0}}}

        result = get_many(campus='test', db=test_database, data=data['courses'], filters=data['filters'])

        self.assertEqual(
            2,
            len(result[0].keys())
        )

    def test_filter_days_will_return_correct_n_courses_with_all_days_set(self):
        data = {
            'courses': [{
                'dept': 'DANC',
                'course': '14'
            }],
            'filters': {
                'days': {
                    'M': 1,
                    'T': 1,
                    'W': 1,
                    'Th': 1,
                    'F': 1,
                    'S': 1,
                    'U': 1
                }
            }
        }

        result = get_many(campus='test', db=test_database, data=data['courses'], filters=data['filters'])
        self.assertEqual(len(result[0].keys()), 2)

    def test_filters_time_returns_n_courses(self):
        data = {'courses':[{'dept':'DANC', 'course':'14'}],
                'filters': {'time':{'start':'7:30 AM', 'end':'12:00 PM'}}}

        result = get_many(campus='test', db=test_database, data=data['courses'], filters=data['filters'])

        self.assertEqual(
            2,
            len(result[0].keys())
        )
