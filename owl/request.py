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
    def __init__(self, *args, user_msg='Bad Request'):
        super().__init__(*args)
        self.user_msg = user_msg


class Request:

    _check_for_unused_args = True  # Able to be changed in subclasses.
    _raise_issues_after_unpacking = True  # Able to be changed in subclasses.

    def __init__(self, *args, **kwargs):
        self.issues: ty.List['Request.Issue'] = []
        self.checked_fields: ty.Dict[str, 'Request.Field'] = {}

        req_args = RequestArguments(*args, **kwargs)
        self.unpack(req_args)

        def check_for_unused_args():
            if not req_args:
                raise TypeError(
                    'Unused arguments can only be detected if request '
                    'arguments are wrapped with a RequestArguments instance. '
                    'This can be done with the wrap_request_arguments '
                    'decorator.')
            for k, v in req_args.unused().items():
                self.issues.append(Request.Issue(k, 'Unused argument.'))

        if self._check_for_unused_args:
            check_for_unused_args()
        if self._raise_issues_after_unpacking and self.issues:
            self.raise_issues()

    def unpack(self, request_args: 'RequestArguments') -> None:
        """
        This method should be overridden by subclasses to define how
        arguments should be unpacked by request.
        :param request_args: RequestArguments
        :return: None
        """
        raise NotImplementedError(
            'unpack() should be overridden by subclasses.')

    def __setattr__(self, k: ty.Any, v: ty.Any):
        """
        If attribute assigned to has same key as a Request.Field
        instance owned by the class, the assigned value is first
        validated by the Field, before being assigned, and any issues
        are added to the collection maintained by Request.
        :param k: str
        :param v: Any
        :return: None
        """
        try:
            field: 'Request.Field' = type(self).__dict__[k]
        except KeyError:
            pass
        else:
            issues = field.validate(v)
            self.issues += issues
        super().__setattr__(k, v)

    def raise_issues(self) -> None:
        """
        Raises a RequestException which contains string representations
        of all issues so far encountered by Request with passed data.
        :return: None
        """
        user_msg = '\n'.join(issue.user_string for issue in self.issues)
        raise RequestException(
            'Issues were encountered during request initialization',
            user_msg=f'The Following issues were encountered'
                     f'while creating request: {user_msg}'
        )

    def __repr__(self) -> str:
        return f'Request[]'

    class Field:
        """
        Class assisting with validation of passed data, to allow better
        feedback to api user.
        """
        def __init__(
                self,
                t: ty.TypeVar = object,
                valid: ty.Container[ty.Any] = (),
                default=None,
                type_coercion=True,
                modifier: ty.Callable[[ty.Any], ty.Any] = None
        ) -> None:
            self.name: str = '<Unnamed Field>'  # Set externally by Request
            self.type = t
            self.valid_values = valid
            self.default = default
            self.type_coercion = type_coercion
            self.modifier = modifier

        def validate(self, value: ty.Any) -> ty.List['Request.Issue']:
            """
            Validates passed value.
            :param value: value that may be assigned to field in a
                        Request instance.
            :return: List[Request.Issue]
            """
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
            """
            Creates a new issue using name of field as Issue
            field param.
            This is intended as a helper method for internal use but
            may also be used externally.
            :param msg: str
            :return: Request.Issue
            """
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

        @property
        def user_string(self) -> str:
            return f'{self.field_name}: {self.msg}'

        def __repr__(self):
            return f'Issue[field: {self.field_name}, msg: {self.msg}]'


class RequestArguments(dict):
    """
    Dictionary subclass that is intended to wrap arguments passed to
    a Request.
    RequestArguments will track which arguments have been used, in
    order to help identify surplus or misnamed fields.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.retrieved = set()

    def __getitem__(self, k):
        self.retrieved.add(k)
        return super().__getitem__(k)

    def unused(self) -> ty.Dict[ty.Any, ty.Any]:
        """
        Returns dictionary of unused keys and their associated values.
        :return: dict
        """
        return {k: v for k, v in self.items() if k not in self.retrieved}
