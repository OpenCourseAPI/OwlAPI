import os
import shutil

from tinydb import TinyDB

# No guarantees can be made about .path when this script is used, so
# use of settings.py is somewhat difficult.
TESTS_DIR = os.path.join(os.path.dirname(__file__))
TEST_DATA_DIR = os.path.join(TESTS_DIR, 'test_db')
TEST_RESOURCES_DIR = os.path.abspath(
    os.path.join(TESTS_DIR, '..', 'test_resources'))
TEST_DATABASE_PATH = os.path.join(TEST_RESOURCES_DIR, 'test_database.json')
test_database = TinyDB(TEST_DATABASE_PATH)


def generate_data_py():
    with open(os.path.join(TEST_DATA_DIR, 'data.py'), 'w') as file:
        # test_sample_url_can_be_generated
        data = {'dept': 'test_dept', 'course': 'test_course'}
        file.write(f"test_sample_url_can_be_generated_data = {data}\n")

        # test_get_one_dept
        data = {'dept': 'CS'}
        dept = test_database.table(f"{data['dept']}").all()
        file.write(f"test_get_one_dept_data = {dept}\n")

        # test_get_one_dept_and_course
        data = {'dept': 'CS', 'course': '2A'}
        dept = test_database.table(f"{data['dept']}").all()
        course = next((e[f"{data['course']}"] for e in dept if
                       f"{data['course']}" in e))
        file.write(f"test_get_one_dept_and_course_data = {course}\n")

        # test_get_two_dept
        data = {'courses': [{'dept': 'CS'}, {'dept': 'MATH'}]}
        depts = []
        for i in data['courses']:
            depts.append(test_database.table(i['dept']).all())
        file.write(f"test_get_two_dept_data = {depts}\n")


def generate_data_model_test_files():
    copies = {
        'model_test_dir_a': (
            '000011',
            '000012',
            '000021',
        )
    }
    # create directories
    for dir_ in copies:
        abs_dir = os.path.join(TEST_RESOURCES_DIR, dir_)
        os.makedirs(abs_dir, exist_ok=True)  # Create path if needed.

        # create test data copies
        for copy_name in copies[dir_]:
            destination = os.path.join(TEST_RESOURCES_DIR, dir_, copy_name)
            destination += '.json'
            shutil.copyfile(TEST_DATABASE_PATH, destination)


def generate_all():
    generate_data_py()
    generate_data_model_test_files()


if __name__ == '__main__':
    generate_all()
