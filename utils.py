from re import match

import click

from settings import COURSE_NAME_PATTERN, COURSE_TYPES_TO_FLAGS

class ValidationError(Exception):
    def __init__(self, message: str, details: str):
        super().__init__(message)

        self.message = message
        self.details = details


def parse_course_str(raw_class: str):
    '''
    This is the key parser for the class/course strings

    :param raw_class: (str) The unparsed string, ex. `C S F001A01Z`
    :return: (dict) the parsed data {'dept', 'course', 'section', 'flags'}
    '''
    # Split the raw course string by a space, to separate different parts
    # ex. 'C S F001A01Z' => ['C', 'S', 'F001A01Z']
    parts = raw_class.split(' ')

    if len(parts) < 2:
        raise ValidationError(
            f"Raw course string ('{raw_class}') is invalid",
            'At least two space separated parts could not be found'
        )

    # All parts excluding the last one are assumed to be part of the department name
    # ex. `C S` => `CS`
    dept = ''.join(parts[0:-1])
    # The last part is the actual course string (without the department)
    # ex. `F001A01Z`
    without_dept = parts[-1]

    if len(without_dept) < 6 or len(without_dept) > 8:
        raise ValidationError(
            f"Invalid course + section string ('{without_dept}')",
            'Length is not between 6-8 chars'
        )

    # First five characters are the course name
    # ex. `D001A` or `F04BH`
    course = without_dept[0:5]
    # Regex to clean the leading 'F'/'D' and extraneous 0's
    match_obj = match(COURSE_NAME_PATTERN, course)

    if not match_obj or not match_obj.groups():
        raise ValidationError(
            f"Unable to extract the course ID (ex. '24A') from '{course}'",
            'Course name regex does not match'
        )

    # Cleaned course name, e.g. `4A`
    cleaned_course = match_obj[1]

    # The last chars are the class section + flags
    # ex. `01Z` or `5ZH`
    section = without_dept[5:]

    # Extract flags by filtering nonalphabets from the class section string
    flags = set(filter(str.isalpha, section))

    return {
        'dept': dept,
        'course': cleaned_course,
        'section': section,
        'flags': flags,
    }


def get_class_type(campus: str, flags: set):
    '''
    From a given set of class flags, return the type of the class

    :param campus: (str) The campus (check COURSE_TYPES_TO_FLAGS)
    :param flags: (set) The flags for the class

    :return: (str) The type of class
    '''
    class_type = None

    for name, flag in COURSE_TYPES_TO_FLAGS[campus].items():
        # Exclude 'standard' because that is the fallback case
        if name != 'standard' and flag in flags:
            if class_type:
                # TODO: should this be a warning instead?
                raise ValidationError('Class has multiple types in its flags', '')
            class_type = name

    if not class_type:
        class_type = 'standard'

    return class_type


def log(tag, color, message, details=None, pad=True):
    '''
    Log a message to stdout

    :param tag: (str) The tag, ex. `info` or `warn`
    :param color: (str) The color for the tag (passed to colorama)
    :param message: (str) The log message string
    :param details: (dict) Extra details to show {'label': 'value'}
    :param pad: (bool) Whether the extra detail lines should be padded
    '''
    formatted_tag = click.style(tag, fg=color, bold=True)
    print(f'{formatted_tag} {message}')

    if details:
        format_label = lambda text: click.style(text, fg='white', dim=True, bold=True)

        for label, msg in details.items():
            padding = len(tag) * ' ' + ' ' if pad else ''
            print(padding + format_label(label), msg)

def log_info(*args, **kwargs):
    '''
    Log an info message (see log())
    '''
    log('info', 'green', *args, **kwargs)

def log_warn(*args, **kwargs):
    '''
    Log a warning (see log())
    '''
    log('warn', 'yellow', *args, **kwargs)

def log_err(*args, **kwargs):
    '''
    Log an error (see log())
    '''
    log('err', 'red', *args, **kwargs)
