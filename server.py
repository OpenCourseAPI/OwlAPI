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
def api_depts():
    return ', '.join(db.tables()), 200


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

        section = next((e[f'{qp_section}'] for e in entries if f'{qp_section}' in e))
        if section:
            return jsonify(section), 200

    return "", 303


if __name__ == "__main__":
    app.run()