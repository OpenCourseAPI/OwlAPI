help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make setup       create virtual environment and install dependencies"
	@echo "    make activate    enter virtual environment"
	@echo "    make test        run the test suite"
	@echo "    exit             leave virtual environment"

setup:
	pip install pipenv
	pipenv install --three

activate:
	pipenv shell

test:
	pipenv shell
	python test/generate_test_data.py
	pipenv run -- pytest test

full: help activate test
