init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

ci:
	pipenv run py.test -n 8 --boxed --junitxml=report.xml
