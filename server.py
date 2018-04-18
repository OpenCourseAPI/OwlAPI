from os.path import join
from collections import defaultdict
from re import match
from crossdomain import add_cors_headers

import itertools as itr

# 3rd party
from quart import Quart, jsonify, request, render_template
from tinydb import TinyDB
from maya import when, MayaInterval

application = Quart(__name__)
application.after_request(add_cors_headers)

DB_ROOT = 'db/'
db = TinyDB(join(DB_ROOT, 'database.json'))

COURSE_PATTERN = 'F0*(\d*\w?)\.?\d*([YWH])?'
DAYS_PATTERN = f"^{'(M|T|W|Th|F|S|U)?'*7}$"

TYPE_ALIAS = {'standard': None, 'online': 'W', 'hybrid': 'Y'}


@application.route('/')
async def idx():
    return await render_template('index.html')


@application.route('/single', methods=['GET'])
async def api_one():
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
    :return: 200 - Found entry and returned data successfully to
                    the user.
    :return: 404 - Could not find entry
    """
    raw = request.args
    qp = {k: v.upper() for k, v in raw.items()}

    data = get_one(qp, filters=dict())
    json = jsonify(data)
    return (json, 200) if data else (
        'Error! Could not find given selectors in database', 404)


@application.route('/batch', methods=['POST'])
async def api_many():
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
    :return: 200 - Found all entries and returned data successfully
                    to the user.
    :return: 404 - Could not find one or more entries.
    """
    raw = await request.get_json()
    data = []

    for course in raw['courses']:
        d = get_one(
            course,
            filters=raw['filters'] if ('filters' in raw) else dict())
        if not d:  # null case from get_one (invalid param or filter)
            return ('Error! Could not find one or more course selectors '
                    'in database', 404)
        data.append(d)

    json = jsonify({'courses': data})
    return json, 200


def get_one(data: dict, filters: dict):
    """
    This is a helper used by the `/get` route to extract course data.
    It works for both [GET] and [POST] and fetches data from the database

    :param data: (dict) The query param or the POST body dict
    :param filters: (dict) A optional dictionary of filters to be
                    passed to filter_courses()
    :return: course: (dict) A singular course listing from the database
                    (if it passes filters)
    """
    data_dept = data['dept']
    if data_dept in db.tables():
        table = db.table(f'{data_dept}')
        entries = table.all()

        if 'course' not in data:
            return entries

        data_course = data['course']

        try:
            course = next((e[f'{data_course}'] for e in entries
                           if f'{data_course}' in e))
            if filters:
                filter_courses(filters, course)

        except StopIteration:
            return dict()
        return course if course else dict()


def filter_courses(filters, course):
    """
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
    def status_filter(course_key):
        # {'open':0, 'waitlist':0, 'full':0}
        if 'status' not in filters:
            return True
        status_mask = {k for (k, v) in filters['status'].items() if v}
        return course[course_key][0]['status'].lower() in status_mask

    def type_filter(course_key):
        # {'standard':1, 'online':1, 'hybrid':0}
        if 'types' not in filters:
            return True
        section = get_key(course[course_key][0]['course'])
        mask = {TYPE_ALIAS[k] for (k, v) in filters['types'].items() if v}
        return section[1] in mask

    def day_filter(course_key):
        # {'M':1, 'T':0, 'W':1, 'Th':0, 'F':0, 'S':0, 'U':0}
        if 'days' in filters:
            # create set of days that are allowed by passed filters
            mask = {k for (k, v) in filters['days'].items() if v}
            for class_ in course[course_key]:
                days_match = match(DAYS_PATTERN, class_['days'])
                course_days = {x for x in days_match.groups() if x} if \
                    days_match else {}
                # Return False if course day is not in mask.
                if not course_days < mask:
                    return False
        return True

    def time_filter(course_key):
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

    def filter_all(k):
        return all((status_filter(k), type_filter(k),
                   day_filter(k), time_filter(k)))

    # remove each key that is evaluated false by filter_all
    for key in itr.filterfalse(filter_all, course.keys.copy()):
        del course[key]


def get_key(key):
    """
    This is the key parser for the course names
    :param key: (str) The unparsed string containing the course name
    :return match_obj.groups(): (list) the string for the regex match
    """
    k = key.split(' ')
    i = 1 if len(k) < 3 else 2
    section = k[i]

    match_obj = match(COURSE_PATTERN, section)
    return match_obj.groups()


@application.route('/list', methods=['GET'])
async def api_list():
    """
    `/list` with [GET] handles a single request to list department or
    course keys from the database
    It takes an optional query parameter `dept` which is first checked
    for existence and then returns the dept keys.
    However, if `course` is also selected, it will return only the data
    of that course within the department.
    :return: 200 - Found entry and returned keys successfully
                to the user.
    :return: 404 - Could not find entry
    """
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


@application.route('/urls', methods=['GET'])
async def api_list_url():
    """
    `/urls` with [GET] returns a tree of all departments, their
    courses, and the courses' endpoints to hit.
    :return: 200 - Should always return
    """
    data = defaultdict(list)

    for dept in db.tables():
        table = db.table(dept)
        keys = set().union(*(d.keys() for d in table.all()))
        data[f'{dept}'].append({k: generate_url(dept, k) for k in keys})

    return jsonify(data), 200


def generate_url(dept: str, course: str) -> str:
    """
    This is a helper
    :param dept:
    :param course:
    :return: dict[str, str]
    """
    return {"dept":f"{dept}", "course":f"{course}"}


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
