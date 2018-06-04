"""
This module contains request classes, which validate and facilitate
access to data passed by api users in get requests.

This module also allows more readable results to api users, that list
any potential issues with their requests, before they are acted on,
and without requiring error code lookups.
"""

import typing as ty

# fields
DEPARTMENT_KEY = 'dept'
COURSE_KEY = 'course'
QUARTER_KEY = 'quarter'

# Argument keywords
ANY = 'any'
ALL = 'all'
LATEST = 'latest'


class RequestException(Exception):
    """
    Exception raised when a request has received bad data.
    RequestException may be given a string to return to the caller
    as part of a 400 error.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.caller_msg = kwargs.get('caller_msg', 'Bad Request')


def throw_issues_after_init(cls: ty.TypeVar):
    return cls


class Request:
    def __init__(self):
        self.issues: ty.List['Request.Issue'] = []
        self.checked_fields: ty.Dict[str, 'Request.Field'] = {}

    def __setattr__(self, k: ty.Any, v: ty.Any):
        if isinstance(v, self.Field):
            v.name = k
            self.checked_fields[k] = v
        else:
            try:
                field = self.checked_fields[k]
            except KeyError:
                pass
            else:
                issues = field.validate(v)
                self.issues += issues
            super().__setattr__(k, v)

    def __repr__(self) -> str:
        return f'GetOneRequest[dept: {self.department}, course: {self.course}]'

    class Field:
        """
        Class assisting with validation of passed data, to allow better
        feedback to api user.
        """
        def __init__(
                self,
                field_type: ty.TypeVar=object,
                valid_values: ty.Collection[ty.Any]=(),
                default=None,
                type_coercion=True,
                modifier: ty.Callable[[ty.Any], ty.Any] = None
        ):
            self.name: str = '<Unnamed Field>'  # Set externally by Request
            self.type = field_type
            self.valid_values = valid_values
            self.default = default
            self.type_coercion = type_coercion
            self.modifier = modifier

        def validate(self, value: ty.Any) -> ty.List['Request.Issue']:
            issues = []

            def validate_type(v: ty.Any) -> 'Request.Issue' or None:
                if isinstance(value, self.type):
                    return None

                if self.type_coercion:
                    try:
                        coerced_value = self.type(value)
                    except (ValueError, TypeError):
                        pass
                    else:
                        if isinstance(coerced_value, self.type):
                            return None
                    return self.issue(
                        f'Cannot coerce passed value: {v} of type: '
                        f'{type(v).__name__} to expected '
                        f'type: {self.type.__name__}.'
                    )
                return self.issue(
                    f'Expected type: {self.type.__name__}, but passed value'
                    f'{v} has type: {type(v).__name__}.')

            def validate_value(v: ty.Any) -> 'Request.Issue' or None:
                try:
                    modified_v = self.modify(v)
                except (ValueError, TypeError):
                    modified_v = v

                if modified_v not in self.valid_values:
                    if modified_v == v:
                        return self.issue(
                            f'Passed value: {v} is not valid. List of valid'
                            f'Values: {self.valid_values}.')
                    else:
                        return self.issue(
                            f'Passed value: {v}, (modified to {modified_v})'
                            f'is not valid. List of valid values: '
                            f'{self.valid_values}.'
                        )
                return None

            if self.type != object:
                issue = validate_type(value)
                if issue:
                    issues.append(issue)

            if self.valid_values:
                issue = validate_value(value)
                if issue:
                    issues.append(issue)

            return issues

        def modify(self, value: ty.Any) -> ty.Any:
            """
            Modifies passed value so that it can be stored in field.
            :param value: Any
            :return: Any
            """
            return self.modifier(value)

        def issue(self, msg: str) -> 'Request.Issue':
            return Request.Issue(self.name, msg)

        def __repr__(self) -> str:
            return f'Request.Field[{self.name}, type: {self.type.__name__}]'

    class Issue:
        """
        Class detailing a specific issue found with a request.
        """

        def __init__(self, field_name: str, msg: str):
            self.field_name = field_name
            self.msg = msg

        def user_string(self) -> str:
            return f'{self.field_name}: {self.msg}'

        def __repr__(self):
            return f'Issue[field: {self.field_name}, msg: {self.msg}]'
