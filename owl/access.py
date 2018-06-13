"""
Intermediary module facilitating access of model.

Methods contained are distinct from those in owl.model because they
are intended primarily for the convenience of the user facing module
(server.py) and contain methods and classes that may result in user-
feedback (eg: AccessException's user_msg and similar).

Methods and classes are separate from server.py because they deal
primarily with access and retrieval of data, and not the form of the
response to the api user's request.
"""
import typing as ty

import owl.model
import owl.filter


# Access Argument keywords
ANY = 'any'
ALL = 'all'
LATEST = 'latest'


class AccessException(ValueError):
    """
    Exception raised when requested data cannot be accessed, but not as
    result of an internal error or bug, or badly a badly formed
    request. This usually is because the requested data does not exist.
    """
    def __init__(self, *args, user_msg='Bad Request'):
        super().__init__(*args)
        self.user_msg = user_msg


class ModelAccessor:
    """
    Handles access of data from a specific data model.
    """
    def __init__(self, model: owl.model.DataModel) -> None:
        self.model = model

    # This method may be removed in the future if the get_one
    # method path is removed.
    def get_one(
            self,
            school: str,
            department: str,
            course: str = ALL,
            quarter: str = LATEST,
            section_filter: owl.filter.SectionFilter = None
    ) -> ty.Union[owl.model.COURSE_DATA_T, owl.model.DEPT_DATA_T]:
        """
        Retrieves data for a department or course, as identified by
        the api user.
        If no course is passed, all of the specified department's data
        is returned.
        :param school: str (ex: 'fh')
        :param department: str (ex: 'CS')
        :param course: str (ex: 1A) (optional)
        :param quarter: str (ex: '201812')
        :param section_filter: filter kwargs
        :return: COURSE_DATA_T or DEPT_DATA_T
        """
        if course == ALL:
            return self.get_department_data(
                school, department, quarter, section_filter)
        return self.get_course_data(
            school, department, course, quarter, section_filter)

    def get_department_data(
            self,
            school: str,
            department: str,
            quarter: str = LATEST,
            section_filter: owl.filter.SectionFilter = None
    ) -> owl.model.DEPT_DATA_T:
        """
        Gets data for a specific department in a single quarter.
        :param school: str (ex: 'fh')
        :param department: str (ex: 'CS')
        :param quarter: str (ex: '201812')
        :param section_filter: filter kwargs
        :return: DEPT_DATA_T
        """
        # Find department view
        department_view = self.get_department(school, department, quarter)

        # get data from department view
        return {
            course_view.name: {
                section_view.crn: section_view.data for
                section_view in course_view.sections if
                not section_filter or section_filter.check(section_view)
            }
            for course_view in department_view.courses
        }

    def get_course_data(
            self,
            school: str,
            department: str,
            course: str,
            quarter: str = LATEST,
            section_filter: owl.filter.SectionFilter = None
    ) -> owl.model.COURSE_DATA_T:
        """
        Gets data for a specific course in a specific quarter.
        :param school: str (ex: 'fh')
        :param department: str (ex: 'CS')
        :param course: str (ex: '1A')
        :param quarter: str (ex: '201812')
        :param section_filter: filter kwargs
        :return: COURSE_DATA_T
        """
        # Find department view
        course_view = self.get_course(school, department, course, quarter)
        return {
            section_view.crn: section_view.data for
            section_view in course_view.sections if
            not section_filter or section_filter.check(section_view)
        }

    def get_quarter(
            self,
            school: str,
            quarter: str = LATEST,
    ) -> 'owl.model.QuarterView':
        """
        Gets QuarterView, throwing readable access errors in the event
        that a passed value is not found.
        :param school: str (ex: 'fh')
        :param quarter: str (ex: '201812')
        :return: QuarterView
        """
        try:
            school_view: owl.model.SchoolView = \
                self.model.schools[school.upper()]
        except KeyError as e:
            raise AccessException(
                f'No school found with identifier: {school}.') from e
        try:
            if quarter == LATEST:
                quarter_view = school_view.latest_quarter
            else:
                quarter_view = school_view.quarters[quarter]
        except KeyError as e:
            raise AccessException(
                f'No quarter in {school} with name: {quarter}.') from e
        return quarter_view

    def get_department(
            self,
            school: str,
            department: str,
            quarter: str = LATEST,
    ) -> owl.model.DepartmentQuarterView:
        """
        Gets department view of department data for a specific quarter.
        :param school: str (ex: 'fh')
        :param department: str (ex: 'CS')
        :param quarter: str (ex: '201812')
        :return: DepartmentQuarterView
        """
        quarter_view = self.get_quarter(school, quarter)
        try:
            department_view = quarter_view.departments[department]
        except KeyError as e:
            raise AccessException(
                f'No department in {quarter} with name: {department}.') from e
        return department_view

    def get_course(
            self,
            school: str,
            department: str,
            course: str,
            quarter: str = LATEST,
    ) -> owl.model.CourseQuarterView:
        department_view = self.get_department(school, department, quarter)
        try:
            course_view = department_view.courses[course]
        except KeyError as e:
            raise AccessException(
                f'No course in {department} with name: {course}.') from e
        return course_view

    def get_section(
            self,
            school: str,
            department: str,
            course: str,
            section: str,
            quarter: str = LATEST,
    ) -> owl.model.SectionQuarterView:
        course_view = self.get_course(school, department, course, quarter)
        try:
            course_view = course_view.courses[course]
        except KeyError as e:
            raise AccessException(
                f'No section in {course} with name: {section}.') from e
        return course_view

    def get_urls(
            self, school: str, quarter: str = LATEST
    ) -> ty.Dict[str, ty.Dict[str, str]]:
        """
        Helps list all courses, their names and departments.
        :param school: str (ex: 'fh')
        :param quarter: str (ex: '201812')
        :return: Dict[str, Dict[str, str]]
        """
        quarter_view = self.get_quarter(school, quarter)
        return {
            department_view.name: {
                course_view.name: {
                    'course': course_view.name,
                    'dept': course_view.department.name
                } for course_view in department_view.courses
            } for department_view in quarter_view.departments
        }
