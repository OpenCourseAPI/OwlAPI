from unittest import TestCase

import os

from settings import TEST_RESOURCES_DIR
from owl.model import DataModel
from owl.access import ModelAccessor

try:
    from tests.test_db import data as test_data
except ImportError as e:
    raise ImportError('Test Data could not be imported. If the data.py file '
                      'does not exist, it can be generated using the '
                      'generate_test_data.py script') from e


class TestGetOne(TestCase):
    def test_get_one_dept(self):
        accessor = get_accessor('model_test_dir_a')
        result = accessor.get_one('fh', department='CS')
        self.assertEqual(
            test_data.test_get_one_dept_data[0],
            result
        )

    def test_get_one_dept_returns_n_courses(self):
        accessor = get_accessor('model_test_dir_a')
        result = accessor.get_one(school='fh', department='CS')
        self.assertEqual(
            len(test_data.test_get_one_dept_data[0].keys()),
            len(result.keys())
        )

    def test_get_one_dept_and_course(self):
        accessor = get_accessor('model_test_dir_a')
        result = accessor.get_one(school='fh', department='CS', course='2A')
        self.assertEqual(
            test_data.test_get_one_dept_and_course_data,
            result
        )


def get_accessor(dir_name: str):
    return ModelAccessor(DataModel(os.path.join(TEST_RESOURCES_DIR, dir_name)))
