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
        if course == ALL:
            return self.get_department_data(
                school, department, quarter, section_filter)
        else:
            return self.get_course_data(
                school, department, course, quarter, section_filter)

    def get_department_data(
            self,
            school: str,
            department: str,
            quarter: str = LATEST,
            section_filter: owl.filter.SectionFilter = None
    ) -> owl.model.DEPT_DATA_T:
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
        # Find department view
        department_view = self.get_department(school, department, quarter)
        try:
            course_view = department_view.courses[course]
        except KeyError as e:
            raise AccessException(
                f'No course in {department} with name: {course}.') from e

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
        quarter_view = self.get_quarter(school, quarter)
        try:
            department_view = quarter_view.departments[department]
        except KeyError as e:
            raise AccessException(
                f'No department in {quarter} with name: {department}.') from e
        return department_view

    def get_urls(
            self, school: str, quarter: str = LATEST
    ) -> ty.Dict[str, ty.Dict[str, str]]:
        quarter_view = self.get_quarter(school, quarter)
        return {
            department_view.name: {
                course_view.name: {
                    'course': course_view.name,
                    'dept': course_view.department.name
                } for course_view in department_view.courses
            } for department_view in quarter_view.departments
        }


def generate_url(dept: str, course: str) -> ty.Dict[str, str]:
    """
    This is a helper function that generates a url string from a passed
    department and course for the /urls route.
    :param dept: str identifier for department
    :param course: str

    :return: dict[str, str]
    """
    return {"dept": f"{dept}", "course": f"{course}"}