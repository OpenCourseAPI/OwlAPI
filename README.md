# FoothilAPI
This is an ~~unofficial~~ API that serves class data from MyPortal to students wishing to use it. You can run it locally by running the steps below.

This project is made portable by [pipenv](http://pipenv.readthedocs.io/en/latest/basics/) - which "harnesses Pipfile, pip, and virtualenv into one single command."

### Contributors
Main contributor: **Kishan Emens**

Other contributors: **Byron White**, **Joshua Fan**, **Jaxon Welsh**

## Setup

**Install pipenv onto root**
> `pip install pipenv`


**Download all dependencies for Foothill API**

Navigate to folder for API then run
> `pipenv install`


**Start pipenv session**
> `pipenv shell`


**Run Data Scraper**
> `python data_scraper.py`


**Start API**
> `python server.py`

## Advanced Setup

**Starting application with gunicorn**
> `gunicorn --worker-class quart.worker.GunicornWorker --bind 0.0.0.0:8000 server:application`
