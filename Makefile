init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

ci:
	pipenv run python tests/generate_test_data.py
	pipenv run pytest tests
