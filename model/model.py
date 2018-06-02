"""
This module contains the data model used by server.py.
"""
import os
import tinydb
import typing as ty
import string
import weakref

DB_EXT = '.json'
SCHOOL_NAMES_BY_CODE = {
    '1': 'FH',
    '2': 'DA'
}
QUARTER_NAMES_BY_CODE = {
    1: 'summer',
    2: 'fall',
    3: 'winter',
    4: 'spring'
}

# Type aliases

COURSE_FIELD_T = str
COURSE_VALUE_T = str
CRN_T = str
COURSE_ID_T = str
DEPT_ID_T = str

SECTION_ENTRY_T = ty.Dict[COURSE_FIELD_T, COURSE_VALUE_T]
SECTION_DATA_T = ty.List[SECTION_ENTRY_T]
COURSE_DATA_T = ty.Dict[CRN_T, SECTION_DATA_T]
DEPT_DATA_T = ty.Dict[str, ty.Dict[COURSE_ID_T, COURSE_DATA_T]]
# todo: Identify this ^^^ str here and what it means.
QTR_DATA_T = ty.Dict[DEPT_ID_T, DEPT_DATA_T]


class DataModel:
    def __init__(self, db_dir: str):
        """
        Initializer for DataModel that uses the passed db_dir path
        to find database tables and store cached values.
        :param db_dir: str path to directory.
        """
        if not os.path.isdir(db_dir):
            raise ValueError(f'Passed path is not a directory: {db_dir}')
        self.db_dir: str = db_dir
        self.quarter_instances = weakref.WeakValueDictionary()
        self.schools = {quarter.school_name: quarter.school
                        for quarter in self.quarters}

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

    @property
    def quarters(self) -> ty.Iterable['QuarterView']:
        """
        Returns generator yielding quarter
        :return:
        """
        for file_name in os.listdir(self.db_dir):
            name, ext = os.path.splitext(file_name)
            if ext != DB_EXT:
                continue  # Ignore non-database files
            if all(c in string.digits for c in name):
                yield QuarterView.get_quarter(self, name)

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
    def quarters(self) -> ty.Iterable['QuarterView']:
        """
        Iterates over and yields views for each quarter that is
        associated with school.
        :return: QuarterView
        """
        for quarter in self.model.quarters:
            if quarter.school == self.name:
                yield quarter

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

    def __init__(self, model: DataModel, name: str):
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
        Database will only be created when this property is accessed,
        and then stored for future uses.
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
        return os.path.join(self.model.db_dir, self.name)

    def __getitem__(self, dept_name: str) -> 'DepartmentView':
        return self.db

    def __repr__(self) -> str:
        return f'QuarterView[{self.name}]'


class DepartmentView:
    """
    View onto data of a specific department
    """

    def __init__(self, model: DataModel, name: str, data: DEPT_DATA_T):
        self.model = model
        self.name = name
        self.data = data


class InstructorView:
    """
    Class handling access of instructor data.
    """
    def __init__(self, model: DataModel, name: str):
        self.model: DataModel = model
        self.name: str = name
