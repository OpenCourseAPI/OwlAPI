import os

from unittest import TestCase

from owl.model import DataModel, QuarterView
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

    def test_department_view_can_be_retrieved_from_quarter(self):
        # This test doesn't help much, but at least confirms that no
        # errors are thrown.
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        self.assertEqual('ACTG', dept.name)
