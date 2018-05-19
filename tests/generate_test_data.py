from os.path import join, dirname, abspath

from tinydb import TinyDB

from sys import path

TEST_DIR = 'tests/test_db'
test_database = TinyDB(join(TEST_DIR, 'test_database.json'))

with open (join(TEST_DIR, 'data.py'), 'w') as file:
    # test_sample_url_can_be_generated
    data = {'dept': 'test_dept', 'course': 'test_course'}

    file.write (f"test_sample_url_can_be_generated_data = {data}\n")

    # test_get_one_dept
    data = {'dept': 'CS'}

    dept = test_database.table(f"{data['dept']}").all()

    file.write (f"test_get_one_dept_data = {dept}\n")

    # test_get_one_dept_and_course
    data = {'dept': 'CS', 'course': '2A'}

    dept = test_database.table(f"{data['dept']}").all()

    course = next((e[f"{data['course']}"] for e in dept if f"{data['course']}" in e))

    file.write (f"test_get_one_dept_and_course_data = {course}\n")

    # test_get_two_dept
    data = {'courses': [{'dept': 'CS'}, {'dept': 'MATH'}]}
    filters = dict()

    depts = []
    for i in data['courses']:
        depts.append(test_database.table(i['dept']).all())

    file.write (f"test_get_two_dept_data = {depts}\n")
