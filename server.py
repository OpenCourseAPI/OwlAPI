from os.path import join, exists
from json import dumps, load

# 3rd party
from quart import Quart, jsonify, request
from tinydb import TinyDB, Query
from tinyTable import TinyTable

app = Quart(__name__)

DB_ROOT = 'db/'
db = TinyDB(join(DB_ROOT, 'database.json'))
db = TinyTable(db)

@app.route('/')
async def hello():
    return 'hello'


@app.route('/list', methods=['GET'])
def api_depts():
    return ', '.join(db.tables()), 200


@app.route('/dept/<dept>', methods=['GET'])
def api_dept(dept):
    table = db.tables(f'{dept}')
    if table:
        return jsonify(table)
    else:
        return "", 404


if __name__ == "__main__":
    app.run()