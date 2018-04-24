from os.path import join, dirname, abspath

from unittest import TestCase
from tinydb import TinyDB

from sys import path
path.append(dirname(dirname(abspath(__file__))))
from server import generate_url, get_one

DB_ROOT = '../test/test_db/'
test_database = TinyDB(join(DB_ROOT, 'database.json'))

class TestGenerateURL(TestCase):
    def test_sample_url_can_be_generated(self):
        self.assertEqual(
            {'dept': 'test_dept', 'course': 'test_course'},
            generate_url('test_dept', 'test_course')
        )

class TestGetOne(TestCase):
    def test_get_one_dept(self):
        data = {'dept': 'CS'}
        dept = test_database.table(f"{data['dept']}").all()

        self.assertEqual(
            dept,
            get_one(data=data, filters=dict(), db=test_database)
        )

    def test_get_one_dept_and_course(self):
        data = {'dept': 'CS', 'course': '2A'}
        dept = test_database.table(f"{data['dept']}").all()
        course = next((e[f"{data['course']}"] for e in dept if f"{data['course']}" in e))

        self.assertEqual(
            course,
            get_one(data=data, filters=dict(), db=test_database)
        )

class TestGetMany(TestCase):
    def test_get_two_dept(self):
        data = {'courses': [{'dept': 'CS'},{'dept': 'MATH'}]}
        depts = {'courses' [test_database.table(f"{data['courses'][0]['dept']}").all()]}
        depts['courses'].append(test_database.table(f"{data['courses'][1]['dept']}").all())

        self.assertEqual(
            depts,
            get_one(data=data, filters=dict(), db=test_database)
        )
