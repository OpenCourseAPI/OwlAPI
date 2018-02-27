from os.path import join

# 3rd party
from quart import Quart, jsonify, request
from tinydb import TinyDB

app = Quart(__name__)

DB_ROOT = 'db/'
db = TinyDB(join(DB_ROOT, 'database.json'))


@app.route('/')
async def hello():
    return 'Foothill API'


@app.route('/list', methods=['GET'])
def api_list():
    '''
    `/list` with [GET] handles a single request to get department or course keys from the database
    It expects a mandatory query parameter `dept` which is first checked for existence and then returns the dept keys.
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

    return f"Error! Could not list (this shouldn't happen)", 404


def get_one(qp: dict()):
    '''
    This is a subfunction used by the `/get` route to extract course data.
    It works for both
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
        except StopIteration:
            return dict()
        if course:
            return course


@app.route('/get', methods=['GET'])
def api_one():
    '''
    `/get` with [GET] handles a single request to get a whole department or a whole course listing from the database
    It expects a mandatory query parameter `dept` and an optionally `course`. ex.{'dept': 'CS', 'course': '2C'}
    If only `dept` is requested, it checked for its existence in the database and then returns it.
    However, if `course` is also selected, it will return only the data of that course within the department.
    :return: 200 - Found entry and returned data successfully to the user.
    :return: 404 - Could not find entry
    '''
    raw = request.args
    qp = {k: v.upper() for k, v in raw.items()}

    data = get_one(qp)
    json = jsonify(data)
    return (json, 200) if data else ('Could not find given selectors in database', 404)


@app.route('/get', methods=['POST'])
async def api_many():
    '''
    `/get` with [POST] handles a batch request to get many departments or a many course listings from the database.
    This batch request is meant to simulate hitting the api route with this data N times.
    It expects a mandatory list of objects containing keys `dept` and `course`.

    Example:
        {
            "courses": [
                {"dept": "MATH", "course": "1A"},
                {"dept": "ENGL", "course": "1A"},
                {"dept": "CHEM", "course": "1A"}
            ]
        }
    :return: 200 - Found all entries and returned data successfully to the user.
    :return: 404 - Could not find one or more entries.
    '''
    raw = await request.get_json()
    data = []

    for qp in raw['courses']:
        d = get_one(qp)
        if not d: #null case from get_one (invalid param)
            return 'Could not find one or more selectors in database', 404
        data.append(d)

    json = jsonify({'courses': data})
    return json, 200


if __name__ == "__main__":
    app.run(debug=True)