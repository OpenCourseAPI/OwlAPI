from os.path import join, exists
from json import dumps, load
from pprint import pprint

# 3rd party
from quart import Quart, jsonify, request
from tinydb import TinyDB, Query

app = Quart(__name__)

DB_ROOT = 'db/'
db = TinyDB(join(DB_ROOT, 'database.json'))


@app.route('/')
async def hello():
    return 'Foothill API'


@app.route('/list', methods=['GET'])
def api_list():
    qp = request.args
    if 'dept' not in qp:
        return jsonify(', '.join(db.tables())), 200

    qp_dept = qp['dept']
    if qp_dept in db.tables():
        table = db.table(f'{qp_dept}')
        keys = set().union(*(d.keys() for d in table.all()))
        return jsonify(', '.join(keys)), 200

    return f"Error! Could not list (this shouldn't happen)", 404


@app.route('/get', methods=['GET'])
def api_dept():
    qp = request.args

    qp_dept = qp['dept']
    if qp_dept in db.tables():
        table = db.table(f'{qp_dept}')
        entries = table.all()

        if 'section' not in qp:
            return jsonify(entries), 200

        qp_section = qp['section']

        try:
            section = next((e[f'{qp_section}'] for e in entries if f'{qp_section}' in e))
        except StopIteration:
            return f'Error! Could not find section: {qp_section}', 404
        if section:
            return jsonify(section), 200

    return f'Error! Could not find department: {qp_dept}', 404


if __name__ == "__main__":
    app.run()