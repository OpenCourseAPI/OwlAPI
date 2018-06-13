"""
Contains classes and methods for filtering data.
"""

import typing as ty
import maya

import owl.model

# Keys
MONDAY_KEY = 'M'
TUESDAY_KEY = 'T'
WEDNESDAY_KEY = 'W'
THURSDAY_KEY = 'Th'
FRIDAY_KEY = 'F'
SATURDAY_KEY = 'S'
SUNDAY_KEY = 'U'

# Filter Argument keywords
ANY = 'any'
ALL = 'all'


class SectionFilter:
    """
    Filters courses based on passed parameters.
    """
    def __init__(
            self,
            status: ty.Dict[str, int] = None,
            types: ty.Dict[str, int] = None,
            days: ty.Dict[str, int] = None,
            time: ty.Dict[str, str] = None,
            instructors: ty.Dict[str, int] = None,
            conflict_sections: ty.Set[owl.model.SectionQuarterView] = None
    ):
        self.status = status
        self.types = types
        self.days = days
        self.time = time
        self.instructors = instructors
        self.conflict_sections = conflict_sections

    def check(self, section: owl.model.SectionQuarterView) -> bool:
        """
        Determines whether passed course passes filter
        :param section: owl.model.SectionQuarterView
        :return: bool (True if section passes filters)
        """

        # Nested functions filter courses by taking a course key and
        # returning a boolean indicating whether they should be included
        # or excluded. True if they are to be included, False if excluded.

        def status_filter() -> bool:
            # {'open':0, 'waitlist':0, 'full':0}
            if not self.status:
                return True
            # Create 'mask' of course statuses that are to be included.
            status_mask = {k for (k, v) in self.status.items() if v}
            # Return True only if course status is in mask.
            return section.status in status_mask

        def type_filter() -> bool:
            # {'standard':1, 'online':1, 'hybrid':0}
            if not self.types:
                return True
            # Get course section
            mask = {k for (k, v) in self.types.items() if v}
            return section.section_type in mask

        def day_filter() -> bool:
            # {'M':1, 'T':0, 'W':1, 'Th':0, 'F':0, 'S':0, 'U':0}
            if not self.days:
                return True
            # create set of days that are allowed by passed filters
            mask = {k for (k, v) in self.days.items() if v}
            return section.days <= mask

        def time_filter() -> bool:
            # {'start':'8:30 AM', 'end':'9:40 PM'}
            if not self.time:
                return True
            filter_range = maya.MayaInterval(
                start=maya.when(self.time['start']),
                end=maya.when(self.time['end']))
            for duration in section.durations:
                if not filter_range.contains(duration.interval):
                    return False
            return True

        def instructor_filter() -> bool:
            if not self.instructors:
                return True
            return section.instructor_name in \
                {k for k, v in self.instructors.items() if v}

        def conflict_filter() -> bool:
            if not self.conflict_sections:
                return True
            for conflict_section in self.conflict_sections:
                if section.conflicts(conflict_section):
                    return False
            return True

        return all((
            status_filter(), type_filter(), day_filter(), time_filter(),
            instructor_filter(), conflict_filter()
        ))
