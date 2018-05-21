## Tests

### Structure:

* One test module for each tested production module

* One TestCase for each class or function to be tested

### Running Tests:

* Generate the test data automatically from `test_database.json` by running
    `tests/generate_test_data.py` from root

* Call pytest on the `tests/` directory. Example: `python3.6 -m pytest tests`
    or use your preferred IDE with pytest support, such as Pycharm
