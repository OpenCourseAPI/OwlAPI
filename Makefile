help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make setup       create virtual environment and install dependencies"
	@echo "    make test        run the test suite"
	@echo "    exit             leave virtual environment"

setup:
    pip install pipenv
    pipenv install --dev
		pipenv shell

test:
    pipenv run pytest test
