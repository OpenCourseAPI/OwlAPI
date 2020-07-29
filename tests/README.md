## Tests

### Structure:

* One test module for each tested production module

* One TestCase for each class or function to be tested

### Running Tests:

* Call pytest on the `tests/` directory. Example: `python3 -m pytest tests`
    or use your preferred IDE with pytest support, such as Pycharm

### Updating Test Database

* To update the test database `db/test_database.json`, run `python3 -m tests.generate_test_db`
