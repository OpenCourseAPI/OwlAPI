import os

from unittest import TestCase

from owl.model import DataModel, DepartmentQuarterView, CourseQuarterView, \
    SectionQuarterView
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
        self.assertIsInstance(dept, DepartmentQuarterView)

    def test_courses_are_accessible_from_department(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        self.assertIsInstance(course, CourseQuarterView)

    def test_sections_are_accessible_from_course(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        section = course.sections['40065']
        self.assertIsInstance(section, SectionQuarterView)
