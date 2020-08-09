from os.path import join
from collections import defaultdict
from re import match

import itertools as itr
import typing as ty

# 3rd party
from flask import Flask, jsonify, request, render_template, send_from_directory
from tinydb import TinyDB
from maya import when, MayaInterval

from utils import parse_course_str, get_class_type
from settings import DAYS_PATTERN, CAMPUS_LIST, DB_DIR


# Flask config
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


application = Flask(__name__,
                    template_folder="frontend/templates", static_folder='frontend/static')
application.after_request(add_cors_headers)


@application.route('/docs/<path:filename>')
def static_docs(filename):
    return send_from_directory('docs', filename)


@application.route('/')
def idx():
    return render_template('index.html')


@application.route('/<campus>/single', methods=['GET'])
def api_one(campus):
    """
    `/single` with [GET] handles a single request to get a whole
    department or a whole course listing from the database
    It expects a mandatory query parameter `dept` and an
    optional `course`.

    Example:
        {'dept': 'CS', 'course': '2C'}

    If only `dept` is requested, it checked for its existence in the
    database and then returns it.
    However, if `course` is also selected, it will return only the data
    of that course within the department.

    :param campus: (str) Campus to retrieve data from.

    :return: 200 - Found entry and returned data successfully to
                    the user.
    :return: 404 - Could not find entry
    """
    if campus not in CAMPUS_LIST:
        return 'Error! Could not find campus in database', 404

    raw = request.args
    qp = {k: v.upper() for k, v in raw.items()}

    db = TinyDB(join(DB_DIR, f'{CAMPUS_LIST[campus]}_database.json'))
    data = get_one(campus, db, qp, filters=dict())
    json = jsonify(data)
    return (json, 200) if data else (
        'Error! Could not find given selectors in database', 404)


@application.route('/<campus>/batch', methods=['POST'])
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
    if campus not in CAMPUS_LIST:
        return 'Error! Could not find campus in database', 404

    db = TinyDB(join(DB_DIR, f'{CAMPUS_LIST[campus]}_database.json'))
    raw = request.get_json()

    data = raw['courses']
    filters = raw['filters'] if ('filters' in raw) else dict()

    courses = get_many(campus=campus, db=db, data=data, filters=filters)
    if not courses:  # null case from get_one (invalid param or filter)
        return 'Error! Could not find one or more course selectors in database', 404

    json = jsonify({'courses': courses})
    return json, 200


def get_one(campus: str, db: TinyDB, data: dict, filters: dict):
    """
    This is a helper used by the `/get` route to extract course data.
    It works for both [GET] and [POST] and fetches data from the database

    :param db: (TinyDB) Database to retrieve data from
    :param data: (dict) The query param or the POST body dict
    :param filters: (dict) A optional dictionary of filters to be
                    passed to filter_courses()

    :return: course: (dict) A singular course listing from the database
                    (if it passes filters)
    """

    course = dict()
    data_dept = data['dept']
    if data_dept in db.tables():
        table = db.table(f'{data_dept}')
        entries = table.all()

        if 'course' not in data:
            # Convert list of `tinydb.table.Document` back to dicts
            return [dict(e) for e in entries]

        data_course = data['course']

        try:
            course = next((dict(e[f'{data_course}']) for e in entries
                           if f'{data_course}' in e))
            if filters:
                filter_courses(campus, filters, course)

        except StopIteration:
            return dict()

    return course


def get_many(campus: str, db: TinyDB, data: dict(), filters: dict()):
    ret = []

    for course in data:
        d = get_one(campus, db, course, filters=filters)
        if not d:  # null case from get_one (invalid param or filter)
            continue
        ret.append(d)

    return ret


def filter_courses(campus, filters: ty.Dict[str, ty.Any], course):
    """
    This is a helper called by get_one() that filters a set of classes
    based on some filter conditionals

    This is a helper called by get_one() that filters a set of classes
    based on some filter conditionals

    Be careful with these as they can be limiting on the data, often
    returning as 404 when one of the courses does not pass the filter.
    Additionally, filters like status and types can be extremely
    limiting on the data. Some courses won't even offer non-online
    classes. Below is an example input with these filters.

    Example filters: {
                'status': {'open':1, 'waitlist':0, 'full':0},
                'types': {'standard':1, 'online':1, 'hybrid':0},
                'days': {'M':1, 'T':0, 'W':1, 'Th':0, 'F':0, 'S':0, 'U':0},
                'time': {'start':'8:30 AM', 'end':'9:40 PM'}
            }

    :param filters: `status` - filter by the availability of a course
                            (Open, Waitlist, Full)
                    `types` - filter by the format of the course
                            (In Person, Online, Hybrid)
                    `days` - filter by the days the course should be
                            limited to (M, T, W, Th, F, S, U)
                    `time` - filter by a specified time interval
                            (8:30 AM - 9:40 PM)
    :param course: (dict) the mutable course listing

    :return: None
    """
    # Nested functions filter courses by taking a course key and
    # returning a boolean indicating whether they should be included
    # or excluded. True if they are to be included, False if excluded.

    def status_filter(course_key) -> bool:
        # {'open':0, 'waitlist':0, 'full':0}
        if 'status' not in filters:
            return True
        # Create 'mask' of course statuses that are to be included.
        status_mask = {k for (k, v) in filters['status'].items() if v}
        # Return True only if course status is in mask.
        return course[course_key][0]['status'].lower() in status_mask

    def type_filter(course_key) -> bool:
        # {'standard':1, 'online':1, 'hybrid':0}
        if 'types' not in filters:
            return True
        # Compute filters
        types = set()
        for k, v in filters['types'].items():
            if not v:
                continue
            types.add(k)
        # Get course flags
        course_str = course[course_key][0]['course']
        flags = parse_course_str(course_str)['flags']
        class_type = get_class_type(campus, flags)
        return class_type in types

    def day_filter(course_key) -> bool:
        # {'M':1, 'T':0, 'W':1, 'Th':0, 'F':0, 'S':0, 'U':0}
        if 'days' in filters:
            # create set of days that are allowed by passed filters
            mask = {k for (k, v) in filters['days'].items() if v}
            for class_ in course[course_key]:
                days_match = match(DAYS_PATTERN, class_['days'])
                course_days = {x for x in days_match.groups() if x} if \
                    days_match else set()
                # Return False if course day is not in mask.
                if not course_days <= mask:
                    return False
        return True

    def time_filter(course_key) -> bool:
        # {'start':'8:30 AM', 'end':'9:40 PM'}
        if 'time' in filters:
            f_range = MayaInterval(
                start=when(filters['time']['start']),
                end=when(filters['time']['end']))
            for class_ in course[course_key]:
                if '-' in class_['time']:
                    data = class_['time'].split('-')
                    class_range = MayaInterval(
                        start=when(data[0]), end=when(data[1]))
                    if not f_range.contains(class_range):
                        return False
        return True

    def filter_all(k) -> bool:
        return all((status_filter(k), type_filter(k),
                   day_filter(k), time_filter(k)))

    # remove each key that is evaluated false by filter_all
    for key in itr.filterfalse(filter_all, set(course.keys())):
        del course[key]


@application.route('/<campus>/list', methods=['GET'])
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

    db = TinyDB(join(DB_DIR, f'{CAMPUS_LIST[campus]}_database.json'))

    raw = request.args
    qp = {k: v.upper() for k, v in raw.items()}

    if 'dept' not in qp:
        return jsonify(', '.join(db.tables())), 200

    qp_dept = qp['dept']
    if qp_dept in db.tables():
        table = db.table(f'{qp_dept}')
        keys = set().union(*(d.keys() for d in table.all()))
        return jsonify(', '.join(keys)), 200

    return 'Error! Could not list', 404


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

    db = TinyDB(join(DB_DIR, f'{CAMPUS_LIST[campus]}_database.json'))

    data = defaultdict(list)

    for dept in db.tables():
        table = db.table(dept)
        keys = set().union(*(d.keys() for d in table.all()))
        data[f'{dept}'].append({k: generate_url(dept, k) for k in keys})

    return jsonify(data), 200


def generate_url(dept: str, course: str) -> ty.Dict[str, str]:
    """
    This is a helper function that generates a url string from a passed
    department and course for the /urls route.
    :param dept: str identifier for department
    :param course: str

    :return: dict[str, str]
    """
    return {"dept": f"{dept}", "course": f"{course}"}


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True, threaded=True)
