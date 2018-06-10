"""
This module contains the data model used by server.py.
"""
import os
import typing as ty
import string
import weakref
import re

import tinydb
import maya

DB_EXT = '.json'
FH = 'FH'
DA = 'DA'
SCHOOL_NAMES_BY_CODE = {
    '1': FH,
    '2': DA
}
QUARTER_NAMES_BY_CODE = {
    1: 'summer',
    2: 'fall',
    3: 'winter',
    4: 'spring'
}
DAYS_PATTERN = f"^{'(M|T|W|Th|F|S|U)?'*7}$"

STANDARD_TYPE = 'standard'
ONLINE_TYPE = 'online'
HYBRID_TYPE = 'hybrid'

SCHOOL_TYPE_CODES = {
    FH: {'W': ONLINE_TYPE, 'Y': HYBRID_TYPE},
    DA: {'Z': ONLINE_TYPE, 'Y': HYBRID_TYPE}
}

# Section fields
COURSE_ID_KEY = 'course'
CRN_KEY = 'CRN'
DESCRIPTION_KEY = 'desc'
STATUS_KEY = 'status'
DAYS_KEY = 'days'
TIME_KEY = 'time'
START_KEY = 'start'
END_KEY = 'end'
ROOM_KEY = 'room'
CAMPUS_KEY = 'campus'
UNITS_KEY = 'units'
INSTRUCTOR_KEY = 'instructor'
SEATS_KEY = 'seats'
WAIT_SEATS_KEY = 'wait_seats'
WAIT_CAP_KEY = 'wait_cap'

# section keywords
ONLINE = 'ONLINE'
OPEN = 'Open'
WAITLIST = 'Waitlist'
FULL = 'Full'
TBA = 'TBA'

# Type aliases

COURSE_FIELD_T = str
COURSE_VALUE_T = str
CRN_T = str
COURSE_ID_T = str
DEPT_ID_T = str

SECTION_ENTRY_T = ty.Dict[COURSE_FIELD_T, COURSE_VALUE_T]
SECTION_DATA_T = ty.List[SECTION_ENTRY_T]
COURSE_DATA_T = ty.Dict[CRN_T, SECTION_DATA_T]
DEPT_DATA_T = ty.Dict[COURSE_ID_T, COURSE_DATA_T]


class DataError(Exception):
    """
    Raised when accessed data cannot be handled.
    Distinct from ValueError because ValueError indicates invalid data
    has been passed, while DataError indicates data that has been
    retrieved from model.
    """


class DataModel:
    def __init__(self, db_dir: str) -> None:
        """
        Initializer for DataModel that uses the passed db_dir path
        to find database tables and store cached values.
        :param db_dir: str path to directory.
        """
        if not os.path.isdir(db_dir):
            raise ValueError(f'Passed path is not a directory: {db_dir}')
        self.db_dir: str = db_dir
        self.quarter_instances = weakref.WeakValueDictionary()
        self.schools = {}  # Populated by generate_data()
        self.quarters = {}  # Populated by generate_data()

        self.generate_data()

    def generate_data(self):
        """
        Generates basic data for DataModel that is kept in memory for
        duration of program or until generate_data is called again to
        update stored data.
        :return: None
        """

        def find_quarters() -> ty.Dict[str, 'QuarterView']:
            """
            Returns dictionary of quarters by name.
            :return: Dict[str code, QuarterView]
            """
            quarters: ty.Dict[str, 'QuarterView'] = {}
            for file_name in os.listdir(self.db_dir):
                name, ext = os.path.splitext(file_name)
                if ext != DB_EXT:
                    continue  # Ignore non-database files
                if all(c in string.digits for c in name):
                    quarters[name] = QuarterView.get_quarter(self, name)
            return quarters

        self.quarters = find_quarters()
        self.schools = {quarter.school_name: quarter.school
                        for quarter in self.quarters.values()}

    def register_quarter(self, quarter: 'QuarterView'):
        """
        Stores weak reference to passed quarter so that in the future,
        the program can avoid creating duplicates of the same quarter.
        :param quarter: QuarterView
        :return: None
        """
        if quarter.model is not self:
            raise ValueError(
                f'Passed quarter {quarter} has model {quarter.model}, '
                f'cannot register it with {self}')
        if quarter.name in self.quarter_instances:
            raise ValueError(f'Passed quarter {quarter} is a duplicate of '
                             f'an existing quarter in {self}.')
        self.quarter_instances[quarter.name] = quarter

    def __repr__(self) -> str:
        return f'DataModel[{self.db_dir}]'


# The reason that the classes below are considered views is that they
# do not contain their own data, and multiple instances may be able to
# be created that all refer to the same data in the model.


class SchoolView:
    """
    Represents a view onto data for a specific school.
    """
    def __init__(self, model: DataModel, name: str):
        if name not in SCHOOL_NAMES_BY_CODE.values():
            raise ValueError(f'Unexpected name received: {name} expected '
                             f'name in {SCHOOL_NAMES_BY_CODE.values()}')
        self.model = model
        self.name = name

    @property
    def quarters(self) -> ty.Dict[str, 'QuarterView']:
        """
        Iterates over and yields views for each quarter that is
        associated with school.
        :return: QuarterView
        """
        return {name: quarter for name, quarter in self.model.quarters if
                quarter.school_name == self.name}

    @property
    def type_codes(self) -> ty.Dict[str, str]:
        """
        Gets dictionary of course section type codes that are specific
        to individual schools.
        :return: Dict[
                        str (course section id suffix),
                        str (course section type)
                    ]
        """
        return SCHOOL_TYPE_CODES[self.name]

    def __repr__(self) -> str:
        return f'SchoolView[{self.name}]'


class QuarterView:
    """
    Represents a view of a specific quarter, for a specific school.
    """
    # In order to avoid loading into memory many duplicates of the same
    # database file, QuarterViews will throw an exception if a
    # duplicate QuarterView is created using the same model + name.
    #
    # To get a QuarterView of a specific quarter, in a specific model,
    # get_quarter() factory method is intended to be used, rather than
    # the constructor.
    #
    # The get_quarter() method will check if the model has a previously
    # stored weak reference to a QuarterView with the same name, and
    # return it if it exists. Otherwise, it creates a new QuarterView,
    # which during its __init__ method, registers itself with
    # the model.

    def __init__(self, model: DataModel, name: str) -> None:
        """
        Instantiates a new QuarterView.
        When instantiated, QuarterView will attempt to register
        itself with its associated model. If a duplicate QuarterView
        exists (with the same model and name) a ValueError is raised.
        :param model: DataModel
        :param name: str
        :raises ValueError if QuarterView is a duplicate.
        """
        self.model: DataModel = model
        self.name: str = name
        self._db: tinydb.TinyDB or None = None  # Loaded lazily (use .db prop)

        # sanity check
        if self.quarter_number not in range(1, 5):  # 1, 2, 3, or 4
            raise ValueError(f'Invalid Quarter number: {self.quarter_number}'
                             f'for {self}')

        # Register QuarterView with model. If QuarterView is a
        # duplicate, then something has gone wrong, and an exception
        # is raised by the method.
        model.register_quarter(self)

    # This factory method might equally have been implemented as an
    # overwritten __new__ method, for more concise instantiation, but
    # the potential for confusion and unintuitive behavior is
    # considered to outweigh the benefit at the time of writing.
    # This balance may change in the future.
    @classmethod
    def get_quarter(cls, model: DataModel, name: str) -> 'QuarterView':
        """
        Returns the quarter of the passed name in the passed model.
        If a QuarterView exists that has already been instantiated
        with the passed name, the pre-existing QuarterView will be
        returned.
        Otherwise, a newly created QuarterView will be returned.
        :param model: DataModel
        :param name: str
        :return: QuarterView
        """
        try:
            return model.quarter_instances[name]
        except KeyError:
            return cls(model, name)

    @property
    def db(self) -> tinydb.TinyDB:
        """
        Database getter;
        Database will only be created when this property is first
        accessed, and will then stored for future uses.
        :return: TinyDB
        """
        if not self._db:
            if not os.path.exists(self.path):
                raise ValueError(
                    f'Path does not exist for {self} in {self.model}')
            self._db = tinydb.TinyDB(self.path)
        return self._db

    @property
    def year(self) -> int:
        """
        Returns school year that quarter occurs in.
        The school year starts with summer and ends with the end of
        spring, and the number represents the calendar year in which
        spring occurs.
        :return: str
        """
        return int(self.name[:4])

    @property
    def quarter_number(self) -> int:
        """
        Returns integer indicating which quarter of the year the
        quarter is.
            1: Summer
            2: Fall
            3: Winter
            4: Spring
        :return: int in range(1, 4) inclusive.
        """
        return int(self.name[4])

    @property
    def quarter_name(self) -> str:
        """
        Returns name of the quarter of the year in which the
        quarter occurs.
            1: Summer
            2: Fall
            3: Winter
            4: Spring
        :return: str
        """
        return QUARTER_NAMES_BY_CODE[self.quarter_number]

    @property
    def school_name(self) -> str:
        """
        Gets name of school as str.
        :return: str 'FH' or 'DA'
        """
        return SCHOOL_NAMES_BY_CODE[self.name[5]]

    @property
    def school(self) -> SchoolView:
        return SchoolView(self.model, self.school_name)

    @property
    def path(self) -> str:
        """
        Gets path to database file which contains quarter data.
        :return: str path
        """
        return os.path.join(self.model.db_dir, self.name) + DB_EXT

    @property
    def departments(self) -> 'Departments':
        """
        Gets helper class that provides methods for accessing
        departments and associated information.
        :return: QuarterView.Departments
        """
        return self.Departments(self)

    def __repr__(self) -> str:
        return f'QuarterView[{self.name}]'

    class Departments:
        """
        Helper class that handles access of department data.
        """
        def __init__(self, quarter: 'QuarterView'):
            self.quarter = quarter

        def __getitem__(self, dept_name: str) -> 'DepartmentQuarterView':
            # screen department names that might otherwise access
            # internal tables, defaults, etc.
            if any(char not in string.ascii_letters for char in dept_name):
                raise ValueError(
                    f'Invalid department name passed: {dept_name}')
            if dept_name not in self.db.tables():
                raise ValueError(
                    f'Passed department name: {dept_name} does not'
                    f'exist in {self}.')

            dept_data: DEPT_DATA_T = self.db.table(dept_name).all()[0]
            return DepartmentQuarterView(self.quarter, dept_name, dept_data)

        @property
        def db(self) -> tinydb.TinyDB:
            return self.quarter.db

        def __repr__(self) -> str:
            return f'{self.quarter}.Departments'


class DepartmentQuarterView:
    """
    View onto data of a department's data for a specific quarter.
    """

    def __init__(self, quarter: 'QuarterView', name: str, data: DEPT_DATA_T):
        self.quarter = quarter
        self.name = name
        self.data = data

        # Sanity Check
        if not 2 <= len(name) <= 4:
            raise Warning(f'Odd department name received: {name}')

    @property
    def model(self):
        return self.quarter.model

    @property
    def courses(self):
        """
        Gets helper class instance for accessing courses
        within department.
        :return: DepartmentQuarterView.Courses
        """
        return self.Courses(self)

    def __repr__(self) -> str:
        return f'DepartmentQuarterView[dept: {self.name}, ' \
               f'qtr: {self.quarter.name}]'

    class Courses:
        """
        Helper class for accessing courses within department.
        """
        def __init__(self, department: 'DepartmentQuarterView'):
            self.department = department

        def __getitem__(self, course_name: str):
            try:
                return CourseQuarterView(
                    self.department,
                    course_name,
                    self.department.data[course_name]
                )
            except KeyError as e:
                raise KeyError(f'No course found named: {course_name} in '
                               f'{self}') from e

        def __repr__(self) -> str:
            return f'{self.department}.Courses'


class CourseQuarterView:
    """
    View onto course data for a single quarter.
    """
    def __init__(
            self,
            department: 'DepartmentQuarterView',
            name: str,
            data: COURSE_DATA_T
    ):
        self.department = department
        self.name = name
        self.data = data

    @property
    def sections(self):
        """
        Gets helper class instance for accessing sections
        within course.
        :return: CourseQuarterView.Sections
        """
        return self.Sections(self)

    def __repr__(self) -> str:
        return f'CourseQuarterView[dept: {self.department.name}, ' \
               f'course: {self.name}]'

    class Sections:
        """
        Helper class for accessing sections within Course
        """
        def __init__(self, course: 'CourseQuarterView'):
            self.course = course

        def __getitem__(self, section_name: str) -> 'SectionQuarterView':
            # If section cannot be found, raise a more readable
            # key error.
            try:
                data = self.course.data[section_name]
            except KeyError as e:
                raise KeyError(f'No Section exists in {self} with id: '
                               f'{repr(section_name)}') from e

            # Get Section from data
            section = SectionQuarterView(self.course, data)
            assert section.crn == section_name, \
                f'section crn: {section.crn} does not match that requested: ' \
                + section_name
            return section

        def __repr__(self):
            return f'{self.course}.Sections'


class SectionQuarterView:
    # All these fields should be equal if multiple entries exist.
    EQUAL_FIELDS = (
        COURSE_ID_KEY, CRN_KEY, DESCRIPTION_KEY, STATUS_KEY, UNITS_KEY,
        INSTRUCTOR_KEY, SEATS_KEY, WAIT_SEATS_KEY, WAIT_CAP_KEY
    )

    def __init__(
            self,
            course: CourseQuarterView,
            data: SECTION_DATA_T
    ):
        self.course = course
        self.data = data

        # Sanity check; Ensure assumptions made about data are true
        for field_name in self.EQUAL_FIELDS:
            if not all(entry[field_name] == self.data[0][field_name] for
                       entry in self.data):
                raise ValueError(
                    f'{self}: {field_name} fields do not match in data')

    @property
    def course_id(self) -> str:
        """
        Returns full identity of section, as listed in database under
        the key 'course' (a somewhat misleading field name).
        'Course' field usually contains department 2-4 letter code,
        Followed by a number indicating Campus, Course id,
        section index, and section type.

        ex: "ACTG F067.03W"
             ^^^^ ^^^^ ^^^
             1111 2333 445

            1: Department code
            2: School
            3: Course id
            4: Section index
            5: Section type ('standard', 'hybrid', or 'online)

        :return: str
        """
        return self.data[0][COURSE_ID_KEY]

    @property
    def crn(self) -> str:
        """
        Gets course registration number for course.
        :return: str of digits of length 5.
        """
        return self.data[0][CRN_KEY]

    @property
    def description(self) -> str:
        """
        Gets description of course.
        This usually takes the form of an all-capital course title,
        ex: "ADVANCED TAX ACCOUNTING I"
        Database spelling may vary.
        :return: str description.
        """
        return self.data[0][DESCRIPTION_KEY]

    @property
    def section_type(self) -> str:
        """
        Returns type of course section.
        :return: str 'standard', 'hybrid' or 'online'
        """
        return self.school.type_codes.get(self.course_id[-1], STANDARD_TYPE)

    @property
    def days(self) -> ty.Set[str]:
        """
        Gets set of days during which class/section meets.
        example result: {'T', 'Th', 'F'}
        :raises DataError if non-online entry has 'TBA' or other value
                    in 'days' field.
        :return: Set[str]
        """
        return {day for entry in self.data
                for day in self._unpack_entry_days(entry)}

    def _unpack_entry_days(self, entry: SECTION_ENTRY_T) -> ty.Set[str]:
        """
        Gets set of days that are listed in passed entry.
        example result: {'T', 'Th', 'F'}
        :param entry: SECTION_ENTRY_T (Dict[str, str])
        :raises DataError if non-online entry has 'TBA' or other value
                    in 'days' field.
        :return: Set[str]
        """
        if entry[ROOM_KEY] == ONLINE:
            # If entry is online, entry will not have a valid room.
            # (usually 'TBA')
            # Return empty set, since no in-persons meetings are in
            # this entry.
            return set()
        s = entry[DAYS_KEY]
        if s == TBA:
            # If days are 'TBA' and class is not online, raise an
            # exception rather than trying to handle odd edge case.
            raise DataError(f'{self} Entry days have not yet been entered')
        matches = re.match(DAYS_PATTERN, entry[DAYS_KEY])
        if not matches:
            raise DataError(f'Could not parse days string: {entry[DAYS_KEY]}')
        days = set(matches.groups()) - {None}
        return days

    @property
    def start_date(self) -> maya.MayaDT:
        """
        Gets start date of class.
        :return: MayaDT
        """
        return maya.when(self.data[0][START_KEY])

    @property
    def end_date(self) -> maya.MayaDT:
        """
        Gets end date of class.
        :return: MayaDT
        """
        return maya.when(self.data[0][END_KEY])

    @property
    def durations(self) -> ty.List['ClassDuration']:
        """
        Gets list of meeting durations, for times over the week that
        a section meets in person.
        :return: List[ClassDuration]
        :raises DataError if unexpected values, such as 'TBA' are found
                    in data entries that are not online.
        """
        durations = []
        for entry in self.data:
            room = entry[ROOM_KEY]
            if room == ONLINE:
                continue
            start_s, end_s = entry[TIME_KEY].split('-')
            start, end = maya.when(start_s), maya.when(end_s)
            for day in self._unpack_entry_days(entry):
                durations.append(ClassDuration(day, room, start, end))
        return durations

    @property
    def rooms(self) -> ty.Set['str']:
        """
        Gets set of rooms (or occasionally other locations) in which
        Set will be empty if course is online.
        :return: Set[str]
        :raises DataError if unexpected values are found in data.
        """
        return {duration.room for duration in self.durations}

    @property
    def status(self) -> str:
        """
        Gets status of course section.
        :return: str 'OPEN', 'WAITLIST', 'FULL'
        """
        return self.data[0][STATUS_KEY]

    @property
    def campus(self) -> str:
        """
        Returns campus code for campus.
        (Not the same thing as 'school').
        :return: str (ex: 'FH')
        """
        return self.data[0][CAMPUS_KEY]

    @property
    def units(self) -> float:
        """
        Gets number of units of course section.
        :return: float
        """
        return float(self.data[0][UNITS_KEY])

    @property
    def instructor_name(self) -> str:
        """
        Gets name of instructor.
        :return: str
        """
        return self.data[0][INSTRUCTOR_KEY]

    @property
    def instructor(self) -> 'InstructorView':
        """
        Gets data view of instructor for this course section.
        :return: InstanceView
        """
        return InstructorView(self.model, self.instructor_name)

    @property
    def open_seats_available(self) -> int:
        """
        Gets number of open seats in course section.
        :return: int
        """
        return int(self.data[0][SEATS_KEY])

    @property
    def waitlist_seats_available(self) -> int:
        """
        Gets number of open waitlist seats in course section.
        :return: int
        """
        return int(self.data[0][WAIT_SEATS_KEY])

    @property
    def waitlist_capacity(self) -> int:
        """
        Gets overall capacity of waitlist, both open and filled.
        :return: int
        """
        return int(self.data[0][WAIT_CAP_KEY])

    @property
    def school_name(self) -> str:
        """
        Gets name of school
        :return: str, (ex: 'DA')
        """
        return self.quarter.school_name

    @property
    def school(self) -> SchoolView:
        """
        Gets course section's school data view.
        :return: SchoolView
        """
        return self.quarter.school

    @property
    def department(self) -> DepartmentQuarterView:
        """
        Gets view of data for department that course section is under.
        :return: DepartmentQuarterView
        """
        return self.course.department

    @property
    def quarter(self) -> QuarterView:
        """
        Gets view of data for quarter that course section
        occurs within.
        :return: QuarterView
        """
        return self.department.quarter

    @property
    def model(self) -> DataModel:
        """
        Gets data model.
        :return: DataModel
        """
        return self.quarter.model

    def __repr__(self) -> str:
        return f'SectionQuarterView[cid: {self.course_id}, crn: {self.crn}]'


class ClassDuration:
    """
    Class storing data about a specific meeting time for a class, on a
    specific day.
    """
    def __init__(
            self,
            day: str,
            room: str,
            start: maya.MayaDT,
            end: maya.MayaDT
    ):
        self.day = day
        self.room = room
        self.interval = maya.MayaInterval(start, end)

    @property
    def start(self):
        return self.interval.start

    @property
    def end(self):
        return self.interval.end


class InstructorView:
    """
    Class handling access of instructor data.
    """
    def __init__(self, model: DataModel, name: str) -> None:
        self.model: DataModel = model
        self.name: str = name
