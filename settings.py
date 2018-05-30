import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
API_DIR = os.path.join(ROOT_DIR, 'owlapi')
DB_DIR = os.path.join(ROOT_DIR, 'db')
TEST_DIR = os.path.join(ROOT_DIR, 'tests')
TEST_DB_DIR = os.path.join(TEST_DIR, 'test_db')
