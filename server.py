"""
This module contains functions for receiving user input and formatting
returned data.
Retrieval logic of data is done in access.py.
"""

# 3rd party
from flask import Flask, jsonify, request, render_template

# Owl modules
# The reason for the relatively verbose imports is to avoid names
# like 'model', 'request' or 'filter' being in the module namespace,
# which may easily be accidentally overridden or mistaken for variables
# of other types.
import settings
import owl.model  # Bring in all objects from model without an ambiguous name.
import owl.input
import owl.access
import owl.filter


# Quart config
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


application = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder='../frontend/static'
)
application.after_request(add_cors_headers)

CAMPUS_LIST = {'fh', 'da'}

# fields
SCHOOL_KEY = 'school'
DEPARTMENT_KEY = 'dept'
COURSE_KEY = 'course'
QUARTER_KEY = 'quarter'
SECTION_KEY = 'section'
FILTER_KEY = 'filters'
FILTER_CONFLICTS_KEY = 'conflict_sections'

data_model = owl.model.DataModel(settings.DB_DIR)
accessor = owl.access.ModelAccessor(data_model)


@application.route('/')
def idx():
    return render_template('index.html')


def basic_checks(input_type=None):
    """
    Wrapper for an api call that handles common exception cases.
    :param input_type:
    :return: Callable
    """
    def decorator(f):
        def api_method_wrapper(*args, **kwargs):
            if input_type:
                inputs = input_type(request)
                if not inputs.validate():
                    return jsonify(success=False, errors=inputs.errors)
            try:
                response = f(*args, **kwargs)
            except owl.access.AccessException as e:
                return e.user_msg, 404  # Data not found
            else:
                return response

        api_method_wrapper.__name__ = f.__name__ + '_wrapper'
        return api_method_wrapper

    return decorator


@application.route('/<campus>/single', methods=['GET'])
@basic_checks(input_type=owl.input.GetOneInput)
def api_one(campus: str):
    """
    `/single` with [GET] handles a single request to get a whole
    department or a whole course listing from the database
    It expects a mandatory query parameter `dept` and an
    optional `course`.

    Example: {'dept': 'CS', 'course': '2C'}

    If only `dept` is requested, it checked for its existence in the
    database and then returns it.
    However, if `course` is also selected, it will return only the data
    of that course within the department.

    :param campus: (str) Campus to retrieve data from.

    :return: 200 - Found entry and returned data successfully to
                    the user.
    :return: 400 - Badly formatted request.
    :return: 404 - Could not find entry.
    """
    # 'campus' refers here to the school, not the physical location,
    # and is not the same thing as the 'campus' field in section data.
    # This is something that should probably be refactored if possible.
    data = accessor.get_one(
        school=campus.upper(),
        quarter=request.args.get(QUARTER_KEY, owl.access.LATEST),
        department=request.args[DEPARTMENT_KEY],  # No default; required field.
        course=request.args.get(COURSE_KEY, owl.access.ALL),
        section_filter=_get_section_filter(request.args),  # May return None.
    )
    return jsonify(data), 200


@application.route('/<campus>/batch', methods=['POST'])
@basic_checks(input_type=owl.input.GetManyInput)
def api_many(campus):
    """
    `/batch` with [POST] handles a batch request to get many
    departments or a many course listings from the database.
    This batch request is meant to simulate hitting the api route with
    this data N times. It expects a mandatory list of objects
    containing keys `dept` and `course`.

    `/batch` also accepts a series of filters that can be applied to
    the results. See filter_courses() for info about what each
    filter does.

    Example Body:
        {
            'courses': [
                {'dept': 'MATH', 'course': '1A'},
                {'dept': 'ENGL', 'course': '1A'},
                {'dept': 'CHEM', 'course': '1A'}
            ],
            'filters': {
                'days': {'M':1, 'T':0, 'W':1, 'Th':0, 'F':0, 'S':0, 'U':0},
                'types': {'standard':1, 'online':1, 'hybrid':0},
                'status': {'open':1, 'waitlist':0, 'full':0},
                'time': {'start':'8:30 AM', 'end':'9:40 PM'}
            }
        }

    :param campus: (str) Campus to retrieve data from

    :return: 200 - Found all entries and returned data successfully
                    to the user.
    :return: 404 - Could not find one or more entries.
    """
    course_filter = _get_section_filter(request.args)

    def get_sub_request_data(args):
        try:
            return accessor.get_one(
                school=campus,
                department=args[DEPARTMENT_KEY],
                course=args.get(COURSE_KEY, owl.access.ALL),
                quarter=args.get(QUARTER_KEY, owl.access.LATEST),
                section_filter=_get_section_filter(args) or course_filter
            )
        except owl.access.AccessException:
            return {}

    data = list(map(get_sub_request_data, request.args['courses']))

    if any(not sub_data for sub_data in data):
        response_code = 404
    else:
        response_code = 200

    json = jsonify({'courses': data})
    return json, response_code


@application.route('/<campus>/list', methods=['GET'])
@basic_checks(input_type=owl.input.GetListInput)
def api_list(campus):
    """
    `/list` with [GET] handles a single request to list department or
    course keys from the database
    It takes an optional query parameter `dept` which is first checked
    for existence and then returns the dept keys.
    However, if `course` is also selected, it will return only the data
    of that course within the department.

    :param campus: (str) The campus to retrieve data from

    :return: 200 - Found entry and returned keys successfully
                to the user.
    :return: 404 - Could not find entry
    """
    if campus not in CAMPUS_LIST:
        return 'Error! Could not find campus in database', 404

    data = accessor.get_one(
        school=campus.upper(),
        quarter=request.args.get(QUARTER_KEY, owl.access.LATEST),
        department=request.args[DEPARTMENT_KEY],  # No default; required field.
        course=request.args.get(COURSE_KEY, owl.access.ALL),
        section_filter=_get_section_filter(request.args),  # May return None.
    ).keys()

    return ('Error! Could not list', 404) if not data else (jsonify(data), 200)


@application.route('/<campus>/urls', methods=['GET'])
def api_list_url(campus):
    """
    `/urls` with [GET] returns a tree of all departments, their
    courses, and the courses' endpoints to hit.

    :param campus: (str) The campus to retrieve data from

    :return: 200 - Should always return
    """
    if campus not in CAMPUS_LIST:
        return 'Error! Could not find campus in database', 404

    data = accessor.get_urls(request.get())

    return jsonify(data), 200


def _get_section_filter(args):
    """
    Produces a SectionFilter from passed arguments
    :param args: request args
    :return: SectionFilter or None
    """
    if not args[FILTER_KEY]:
        return None
    filter_kwargs = args.copy()
    try:
        conflict_sections = filter_kwargs[FILTER_CONFLICTS_KEY]
    except KeyError:
        pass
    else:
        # replace filter conflicts identifiers with set of
        # section views.
        filter_kwargs[FILTER_CONFLICTS_KEY] = {
            accessor.get_section(
                school=section_identifiers[SCHOOL_KEY],
                quarter=section_identifiers[QUARTER_KEY],
                department=section_identifiers[DEPARTMENT_KEY],
                course=section_identifiers[COURSE_KEY],
                section=section_identifiers[SECTION_KEY]
            ) for section_identifiers in conflict_sections
        }
    return owl.filter.SectionFilter(**filter_kwargs)


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True, threaded=True)
