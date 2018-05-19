## Tests

### Structure:

* One test module for each tested production module

* One TestCase for each class or function to be tested

### Running Tests:

* Generate the test data automatically from `test_database.json` by running
    `generate_test_data.py` from this folder

* Call pytest on the `test/` directory. Example: `python3.6 -m pytest test`
    or use your preferred IDE with pytest support, such as Pycharm
