import os

from unittest import TestCase

from model.model import DataModel, QuarterView
from tests.generate_test_data import TEST_RESOURCES_DIR


class TestDataModel(TestCase):
    def test_model_finds_all_tables(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        self.assertEqual(3, len([quarter for quarter in data.quarters]))

    def test_model_contains_correct_schools(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        self.assertEqual(2, len(data.schools))
        self.assertIn('FH', data.schools)
        self.assertIn('DA', data.schools)
