from os.path import join
from unittest import TestCase, SkipTest

from tinydb import TinyDB

import settings
from server import generate_url

# Try to get generated data.
try:
    from tests.test_db import data as test_data
except ImportError as e:
    raise ImportError('Test Data could not be imported. If the data.py file '
                      'does not exist, it can be generated using the '
                      'generate_test_data.py script') from e

test_database = TinyDB(join(settings.TEST_RESOURCES_DIR, 'test_database.json'))


class TestGenerateURL(TestCase):
    def test_sample_url_can_be_generated(self):
        self.assertEqual(
            test_data.test_sample_url_can_be_generated_data,
            generate_url('test_dept', 'test_course')
        )

