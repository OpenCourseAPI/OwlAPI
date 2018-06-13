from unittest import TestCase

from .test_model import get_test_data_dir

from owl.model import DataModel
from owl.access import ModelAccessor

try:
    from tests.test_db import data as test_data
except ImportError as e:
    raise ImportError('Test Data could not be imported. If the data.py file '
                      'does not exist, it can be generated using the '
                      'generate_test_data.py script') from e


class TestAccessor(TestCase):
    def test_get_one_dept(self):
        with get_test_data_dir('model_test_dir_a') as data_dir:
            accessor = get_accessor(data_dir)
            result = accessor.get_one('fh', department='CS')
            self.assertEqual(
                test_data.test_get_one_dept_data[0],
                result
            )

    def test_get_one_dept_returns_n_courses(self):
        with get_test_data_dir('model_test_dir_a') as data_dir:
            accessor = get_accessor(data_dir)
            result = accessor.get_one(school='fh', department='CS')
            self.assertEqual(
                len(test_data.test_get_one_dept_data[0].keys()),
                len(result.keys())
            )

    def test_get_one_dept_and_course(self):
        with get_test_data_dir('model_test_dir_a') as data_dir:
            accessor = get_accessor(data_dir)
            result = accessor.get_one(school='fh', department='CS', course='2A')
            self.assertEqual(
                test_data.test_get_one_dept_and_course_data,
                result
            )

    def test_get_urls_gets_all_departments(self):
        with get_test_data_dir('model_test_dir_a') as data_dir:
            accessor = get_accessor(data_dir)
            result = accessor.get_urls(school='fh', quarter='000011')
            self.assertEqual(74, len(result))


def get_accessor(dir_name: str):
    return ModelAccessor(DataModel(dir_name))
