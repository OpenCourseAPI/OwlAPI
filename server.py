from os.path import join
from collections import defaultdict
from re import search

# 3rd party
from quart import Quart, jsonify, request, render_template
from tinydb import TinyDB

application = Quart(__name__)

DB_ROOT = 'db/'
db = TinyDB(join(DB_ROOT, 'database.json'))
DAY_MATCH = f"^{'(M|T|W|Th|F|S|U)?'*7}$"


@application.route('/')
async def idx():
    return await render_template('index.html')


@application.route('/single', methods=['GET'])
async def api_one():
    '''
    `/single` with [GET] handles a single request to get a whole department or a whole course listing from the database
    It expects a mandatory query parameter `dept` and an optionally `course`.

    Example:
        {'dept': 'CS', 'course': '2C'}

    If only `dept` is requested, it checked for its existence in the database and then returns it.
    However, if `course` is also selected, it will return only the data of that course within the department.
    :return: 200 - Found entry and returned data successfully to the user.
    :return: 404 - Could not find entry
    '''
    raw = request.args
    qp = {k: v.upper() for k, v in raw.items()}

    data = get_one(qp, dict())
    json = jsonify(data)
    return (json, 200) if data else ('Error! Could not find given selectors in database', 404)


@application.route('/batch', methods=['POST'])
async def api_many():
    '''
    `/batch` with [POST] handles a batch request to get many departments or a many course listings from the database.
    This batch request is meant to simulate hitting the api route with this data N times.
    It expects a mandatory list of objects containing keys `dept` and `course`.

    Example Body:
        {
            "courses": [
                {"dept": "MATH", "course": "1A"},
                {"dept": "ENGL", "course": "1A"},
                {"dept": "CHEM", "course": "1A"}
            ],
            "filters": {
                "campus": "FH",
                "days": {"M":1, "T":0, "W":1, "Th":0, "F":0, "S":0, "U":0},
                "type": {"standard":1, "online":1, "hybrid":0},
                "status": "Open",
                "time": "01:30 PM-03:20 PM"
            }
        }
    :return: 200 - Found all entries and returned data successfully to the user.
    :return: 404 - Could not find one or more entries.
    '''
    raw = await request.get_json()
    data = []

    for course in raw['courses']:
        d = get_one(course, filters=raw['filters'] if ('filters' in raw) else dict())
        if not d:  # null case from get_one (invalid param)
            return 'Error! Could not find one or more course selectors in database', 404
        data.append(d)

    json = jsonify({'courses': data})
    return json, 200


def get_one(qp: dict, filters: dict):
    '''
    This is a helper used by the `/get` route to extract course data.
    It works for both [GET] and [POST] and fetches data from the database
    :return:
    '''
    qp_dept = qp['dept']
    if qp_dept in db.tables():
        table = db.table(f'{qp_dept}')
        entries = table.all()

        if 'course' not in qp:
            return entries

        qp_course = qp['course']

        try:
            course = next((e[f'{qp_course}'] for e in entries if f'{qp_course}' in e))
            if filters:
                for key in course.copy():
                    # 'Full' 'Waitlist' 'Open'
                    if 'status' in filters:
                        if course[key][0]['status'] != filters['status']:
                            course.pop(key, None)
                            continue

                    # {"M":1, "T":0, "W":1, "Th":0, "F":0, "S":0, "U":0}
                    if 'days' in filters:
                        filtered_days = {k for (k, v) in filters['days'].items() if v == 1}
                        course_days = set()
                        for c in course[key]:
                            days_match = search(DAY_MATCH, c['days'])
                            if days_match:
                                course_days = course_days.union({x for x in days_match.groups() if x is not None})

                        if course_days:
                            union = filtered_days & course_days
                            if len(course_days) > len(union):
                                course.pop(key, None)
                                continue

            if not course:
                assert StopIteration

        except StopIteration:
            return dict()
        if course:
            return course


@application.route('/list', methods=['GET'])
async def api_list():
    '''
    `/list` with [GET] handles a single request to list department or course keys from the database
    It takes an optional query parameter `dept` which is first checked for existence and then returns the dept keys.
    However, if `course` is also selected, it will return only the data of that course within the department.
    :return: 200 - Found entry and returned keys successfully to the user.
    :return: 404 - Could not find entry
    :return:
    '''
    raw = request.args
    qp = {k: v.upper() for k, v in raw.items()}

    if 'dept' not in qp:
        return jsonify(', '.join(db.tables())), 200

    qp_dept = qp['dept']
    if qp_dept in db.tables():
        table = db.table(f'{qp_dept}')
        keys = set().union(*(d.keys() for d in table.all()))
        return jsonify(', '.join(keys)), 200

    return "Error! Could not list", 404

def generate_url(dept: str, course: str):
    '''
    This is a helper
    :param dept:
    :param course:
    :return:
    '''
    return f"get?dept={dept}&course={course}"

@application.route('/urls', methods=['GET'])
async def api_list_url():
    '''
    `/urls` with [GET] returns a tree of all departments, their courses, and the courses' endpoints to hit.
    :return: 200 - Should always return
    '''
    data = defaultdict(list)

    for dept in db.tables():
        table = db.table(dept)
        keys = set().union(*(d.keys() for d in table.all()))
        data[f'{dept}'].append({k: generate_url(dept, k) for k in keys})

    return jsonify(data), 200

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
