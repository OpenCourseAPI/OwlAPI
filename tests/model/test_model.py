import os

from unittest import TestCase

import maya

from owl.model import DataModel, DepartmentQuarterView, CourseQuarterView, \
    SectionQuarterView, ClassDuration, \
    OPEN, STANDARD_TYPE, ONLINE_TYPE, HYBRID_TYPE
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

    def test_section_course_id_returns_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        section = course.sections['40065']
        self.assertEqual('ACTG F001A02Y', section.course_id)

    def test_section_crn_returns_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        section = course.sections['40065']
        self.assertEqual('40065', section.crn)

    def test_section_description_returns_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        section = course.sections['40065']
        self.assertEqual('FINANCIAL ACCOUNTING I', section.description)

    def test_section_status_returns_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1B']
        section = course.sections['41130']
        self.assertEqual(OPEN, section.status)

    def test_section_days_returns_correctly_in_semi_online_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        section = course.sections['40065']
        self.assertEqual({'T', 'Th'}, section.days)

    def test_section_days_property_raises_exception_in_online_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        section = course.sections['40018']
        self.assertEqual(set(), section.days)

    def test_section_days_returns_correctly_in_offline_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ENGL']
        course = dept.courses['1A']
        section = course.sections['40140']
        self.assertEqual({'M', 'W'}, section.days)

    def test_section_days_returns_correctly_in_single_day_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['76']
        section = course.sections['41440']
        self.assertEqual({'W'}, section.days)

    def test_section_days_returns_correctly_in_class_with_labs_a(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['PHYS']
        course = dept.courses['2B']
        section = course.sections['40582']
        self.assertEqual({'T', 'Th'}, section.days)

    def test_section_days_returns_correctly_in_class_with_labs_b(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['PHYS']
        course = dept.courses['4D']
        section = course.sections['40208']
        self.assertEqual({'T', 'Th', 'F'}, section.days)

    def test_section_durations_return_correct_maya_date_times(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['PHYS']
        course = dept.courses['4D']
        section = course.sections['40208']
        durations = section.durations
        self.assertEqual(4, len(durations))
        self.assertIsInstance(durations[0], ClassDuration)
        self.assertIsInstance(durations[1], ClassDuration)
        self.assertIsInstance(durations[2], ClassDuration)
        self.assertIsInstance(durations[3], ClassDuration)

        # Check that each duration has expected times
        for duration in durations:
            if duration.day == 'Th':
                self.assertEqual(maya.when('10:00AM'), duration.start)
                self.assertEqual(maya.when('11:50AM'), duration.end)
            elif duration.day == 'F':
                self.assertEqual(maya.when('11:00 AM'), duration.start)
                self.assertEqual(maya.when('11:50AM'), duration.end)

    def test_section_rooms_are_found_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['PHYS']
        course = dept.courses['4D']
        section = course.sections['40208']
        durations = section.durations
        self.assertIsInstance(durations[0], ClassDuration)
        self.assertIsInstance(durations[1], ClassDuration)
        self.assertIsInstance(durations[2], ClassDuration)
        self.assertIsInstance(durations[3], ClassDuration)

        # Check that each duration has expected times
        for duration in durations:
            if duration.day == 'Th':
                self.assertEqual('4501', duration.room)
            elif duration.day == 'F':
                self.assertEqual('4501', duration.room)
            elif duration.day == 'T' and \
                    duration.start == maya.when('12:00PM'):
                self.assertEqual('4718', duration.room)

    def test_section_rooms_are_found_correctly_for_multi_room_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['PHYS']
        course = dept.courses['4D']
        section = course.sections['40208']
        self.assertEqual({'4718', '4501'}, section.rooms)

    def test_section_rooms_are_found_correctly_for_single_room_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1B']
        section = course.sections['40067']
        self.assertEqual({'3201'}, section.rooms)

    def test_section_rooms_are_found_correctly_for_online_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1C']
        section = course.sections['40022']
        self.assertEqual(set(), section.rooms)

    def test_section_end_returns_correct_maya_date(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ENGL']
        course = dept.courses['1A']
        section = course.sections['40140']
        end_date = section.end_date
        self.assertIsInstance(end_date, maya.MayaDT)

    def test_section_type_is_determined_correctly_for_offline_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ENGL']
        course = dept.courses['1A']
        section = course.sections['40140']
        self.assertEqual(STANDARD_TYPE, section.section_type)

    def test_section_type_is_determined_correctly_for_online_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        section = course.sections['40018']
        self.assertEqual(ONLINE_TYPE, section.section_type)

    def test_section_type_is_determined_correctly_for_hybrid_class(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1A']
        section = course.sections['40065']
        self.assertEqual(HYBRID_TYPE, section.section_type)

    def test_section_campus_is_found_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1B']
        section = course.sections['40067']
        self.assertEqual('FH', section.campus)

    def test_section_units_are_found_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1B']
        section = course.sections['40067']
        self.assertEqual(5, section.units)

    def test_section_instructor_name_returns_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1B']
        section = course.sections['40067']
        self.assertEqual('Drake', section.instructor_name)

    def test_section_seats_return_correctly_when_on_waitlist_status(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1B']
        section = course.sections['40067']
        self.assertEqual(0, section.open_seats_available)

    def test_section_wait_seats_return_correctly_when_on_waitlist_status(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1B']
        section = course.sections['40067']
        self.assertEqual(7, section.waitlist_seats_available)

    def test_section_waitlist_capacity_returns_correctly(self):
        data = DataModel(os.path.join(TEST_RESOURCES_DIR, 'model_test_dir_a'))
        quarter = data.quarters['000011']
        dept = quarter.departments['ACTG']
        course = dept.courses['1B']
        section = course.sections['40067']
        self.assertEqual(15, section.waitlist_capacity)
