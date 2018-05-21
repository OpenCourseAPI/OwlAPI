# OwlAPI
This is an unofficial API that serves course data from Foothill DeAnza MyPortal to students wishing to use it. If you have a suggestion for what other FHDA data this API should serve, drop an issue on Github. OwlAPI now has a home at [floof.li](https://floof.li).

#### Contributors:
> [**Kishan Emens**](https://github.com/phi-line), [John Schwarz](https://github.com/TryExceptElse), [Joshua Kuan](https://github.com/cwjoshuak), [Joshua Fan](https://github.com/joshuaptfan), [Byron White](https://github.com/BoomSyrup)

If you would like to contribute follow this [guide](https://github.com/FoothillCSClub/OwlAPI/blob/master/CONTRIBUTING.md).

#### Applications powered by OwlAPI:
> [**FHDA Class Register**](https://github.com/cwjoshuak/FHDA-Class-Register), [SchedOWL](https://github.com/FoothillCSClub/SchedOwl)


#### Dependencies:
> [Quart](https://gitlab.com/pgjones/quart), [TinyDB](https://github.com/msiemens/tinydb), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/), [Requests](https://github.com/requests/requests), [Maya](https://github.com/kennethreitz/maya) ✨🍰✨

## Data overview
OwlAPI serves data directly from MyPortal. It does not try to filter or add anything new to the format to maintain purity to the original. For now, only the most recent quarter's data is pulled from MyPortal. Below the various data points are listed and described:

### JSON data
```
CRN        | Course Number
course     | Course ID (format: [F0*][ID][Section ID][WYH]) see note
desc       | Short-form course description
campus     | Campus the section is held at
days       | Day(s) the section is held on (M, T, W, Th, F, S, U)
instructor | Professor for the section
room       | Room the section is held at
time       | Time for the section
start      | First date for the section
end        | Last date for the course
units      | Number of course units
seats      | Seats left in the course
status     | Status of the course (Online / Waitlist)
wait_cap   | Waitlist capacity
wait_seats | Waitlist slots left in the course
```
#### Course variant format
```
Online     | W (Foothill) / Z (De Anza)
Hybrid     | Y
Honors     | H
```

On [floof.li](https://floof.li), seat data is synced every 5 minutes with MyPortal.

### Campus selector
Before any of the endpoints below, you must select which campus' data you'd like the query. Before the endpoint type `/fh` or `/da` for Foothill and De Anza respectively.

Alternatively, if either campus' data cannot be accessed, a debug campus has been put into production. Use the
campus selector `test` to grab this older copy of Foothill data.

> `GET /fh/list?dept=CS`
```
2C, 49, 30A, 80A, 18, 21B, 50E, 3A, 22A, 50C, 50A, 20A, 2A, 1B, 1A, 81A, 53A, 82A, 30B, 63A, 21A, 53B, 1C, 2B, 10, 31A, 60A
```

## Endpoints
### Get single
`GET /single` handles a single request to get a whole department or a whole course listing from the database
It expects a mandatory query parameter `dept` and an optionally `course`.

> `GET /fh/single?dept=CS&course=2A`
```
{"10116":
	[
		{ "CRN": "10116",
			"campus": "FH",
			"course": "C S F002A01W",
			"days": "TBA",
			"desc": "OBJ-ORIENT PROG METHOD IN C++",
			"end": "08/12/2018",
			"instructor": "Venkataraman",
			"room": "ONLINE",
			"seats": "34",
			"start": "07/02/2018",
			"status": "Open",
			"time": "TBA",
			"units": "4.50",
			"wait_cap": "10",
			"wait_seats": "10" },
		{...}
	]
}
```

You can view an example of the `/single` route [here](https://github.com/FoothillCSClub/OwlAPI/tree/master/examples/single).

<div id="interact"><div data-request-type="GET" data-request-url="/fh/single" data-request-body="?dept=CS&course=2A"></div></div>

### Get batch
`POST /batch` handles a batch request to get many departments or many sections from the database.
This batch request is meant to simulate hitting the api route with this data N times.
It expects a mandatory list of objects containing keys `dept` and `course`.

> `POST /fh/batch`
```
{
  "courses": [
    {"dept":"CS", "course":"1A"},
    {"dept":"MATH", "course":"1A"},
    {"dept":"ENGL", "course":"1A"}
  ]
}
```

<div id="interact"><div data-request-type="POST" data-request-url="/fh/batch" data-request-body='{"courses":[{"dept":"CS","course":"2A"},{"dept":"MATH","course":"1A"},{"dept":"ENGL","course":"1A"}]}'></div></div>

### Filters
Additionally, in the `POST /batch` body you can specify any number of filters to narrow the results. Add the filter key to the post body and then apply the appropriate filter. Multiple options can be selected by changing the value from a `0` to a `1`.
Be careful because too many filters may result in zero sections returned from the database. Also, even if 2 out of 3 courses are valid, one invalid will return `404`.

#### Filter by status
Filter by the availability of a course (Open, Waitlist, Full). The example below shows how you can filter only `open` and `waitlist` sections.

> `POST /fh/batch`
```
{
  "courses": [{"dept":"CS", "course":"1A"}]
  "filters": {"status": {"open":1, "waitlist":1, "full":0}}
}
```

<div id="interact"><div data-request-type="POST" data-request-url="/fh/batch" data-request-body='{"courses":[{"dept":"CS","course":"2A"}], "filters":{"status":{"open":1, "waitlist":1, "full":0}}}'></div></div>


#### Filter by type
Filter by the format of the course (In Person, Online, Hybrid). The example below shows how you can filter only `online` and `hybrid` sections.

> `POST /fh/batch`
```
{
  "courses": [{"dept":"CS", "course":"1A"}]
  "filters": {"types":{"standard":0, "online":1, "hybrid":1}}
}
```

<div id="interact"><div data-request-type="POST" data-request-url="/fh/batch" data-request-body='{"courses":[{"dept":"CS","course":"2A"}], "filters":{"types":{"standard":0, "online":1, "hybrid":1}}}'></div></div>


#### Filter by days
Filter by the days the course should be limited to (M, T, W, Th, F, S, U). The example below shows how you can filter only `M` and `W` sections.

> `POST /fh/batch`
```
{
  "courses": [{"dept":"CS", "course":"1A"}]
  "filters": {"days":{"M":1, "T":0, "W":1, "Th":0, "F":0, "S":0, "U":0}}
}
```

<div id="interact"><div data-request-type="POST" data-request-url="/fh/batch" data-request-body='{"courses":[{"dept":"CS","course":"2A"}], "filters":{"days":{"M":1, "T":0, "W":1, "Th":0, "F":0, "S":0, "U":0}}}'></div></div>


#### Filter by time
Filter by a specified time interval (7:30 AM - 12:00 PM). The example below shows how you can filter only morning sections.

> `POST /fh/batch`
```
{
  "courses": [{"dept":"CS", "course":"1A"}]
  "filters": {"time":{"start":"7:30 AM", "end":"12:00 PM"}}
}
```

<div id="interact"><div data-request-type="POST" data-request-url="/fh/batch" data-request-body='{"courses":[{"dept":"CS","course":"2A"}], "filters":{"time":{"start":"7:30 AM", "end":"12:00 PM"}}}'></div></div>


### List
`GET /list` handles a single request to list department or course keys from the database
It takes an optional query parameter `dept` which is first checked for existence and then returns the dept keys.

> `GET /fh/list`
```
IDS, CHLD, ALTW, ANTH, SPAN, CRWR, DH, NCLA, POLI, CHEM, CNSL, GIST, MTEC, ASTR, PHOT, ITRN, DMS, AHS, EMTP, ATHL, APEL, HIST, HORT, GEOG, SPED, ALCB, RT, MDIA, ENGR, THTR, NCSV, NCBS, ACTG, NCEL, KINS, DANC, HUMN, DA, JAPN, CRLP, VITI, BIOL, BUSI, PSE, _default, ECON, RSPT, ART, NCBH, PHT, LA, CS, LINC, MUS, EMS, PHED, ENGL, VT, HLTH, APPT, MATH, COMM, NCP, GID, LIBR, APSM, PHDA, PHIL, WMN, NANO, PSYC, ESLL, SOC, APIW, PHYS
```

> `GET /fh/list?dept=CS`
```
2C, 49, 30A, 80A, 18, 21B, 50E, 3A, 22A, 50C, 50A, 20A, 2A, 1B, 1A, 81A, 53A, 82A, 30B, 63A, 21A, 53B, 1C, 2B, 10, 31A, 60A
```

<div id="interact"><div data-request-type="GET" data-request-url="/fh/list" data-request-body="?dept=CS"></div></div>


### URLs
`GET /urls` returns a tree of all departments, their courses, and the courses' endpoints to hit.

> `GET /fh/urls`
```
"CS": [
  {
    "2A": {
      "course": "2A",
      "dept": "CS"
    },
    "2B": {
      "course": "2B",
      "dept": "CS"
    },
    "2C": {
      "course": "2C",
      "dept": "CS"
    },
    {...}
  }
],
"MATH": [...]
```

<div id="interact"><div data-request-type="GET" data-request-url="/fh/urls" data-request-body=""></div></div>

## Setup
### Local setup

**Install pipenv onto root**
> `pip install pipenv`


**Download all dependencies for Foothill API**
> `pipenv install`


**Start pipenv session**
> `pipenv shell`


**Run Data Scraper**
> `python data_scraper.py`


**Start API**
> `python server.py`


### Server setup
This is a setup guide for using [`systemctl`](https://www.freedesktop.org/software/systemd/man/systemctl.html) to run the server in the background. This small guide also covers how to setup a servive to refresh the database on timed interval.

#### OwlAPI service
This service is the main driver which runs the API. Gunicorn is used to serve Python through [`WSGI`](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), and [`nginx`](https://www.nginx.com/) is used to direct port traffic to The API.

**Create a file named OwlAPI.service**
> `sudo vi /etc/systemd/system/OwlAPI.service`

**Paste in this sample config changing `user`**
```
[Unit]
Description=Gunicorn instance to serve OwlAPI
After=network.target

[Service]
User=user
Group=nginx
WorkingDirectory=/home/user/OwlAPI
Environment="PATH=/home/user/.local/share/virtualenvs/OwlAPI-mya9jbVn/bin/"
ExecStart=/home/user/.local/share/virtualenvs/OwlAPI-mya9jbVn/bin/gunicorn --workers 3 --worker-class quart.worker.GunicornWorker --bind 0.0.0.0:8000 -m 007 server:application

[Install]
WantedBy=multi-user.target
```
You'll also have to change the virtualenv path to match the id from when you ran `pipenv shell`

**Start and enable the service**
> `sudo systemctl start OwlAPI`

> `sudo systemctl enable OwlAPI`

#### Database refresh service
This service runs in the background to refresh the database on a timed interval. This keeps the API fresh with new data from MyPortal. It's crucial to have the data refreshed if live course seat and status data is desired.

**Create a file named refreshDB.service**
> `sudo vi /etc/systemd/system/refreshDB.service`

**Paste in this sample config changing `user`**
```
[Unit]
Description=Timer job to refresh OwlAPI database
After=network.target

[Service]
User=user
Type=simple
WorkingDirectory=/home/user/OwlAPI
Environment=PATH=/home/user/.local/share/virtualenvs/OwlAPI-mya9jbVn/bin/
ExecStart=/home/user/.local/share/virtualenvs/OwlAPI-mya9jbVn/bin/python3.6 /home/user/OwlAPI/data_scraper.py
StandardError=journal

[Install]
WantedBy=multi-user.target
```

**Create a file named refeshDB.timer**
> `sudo vi /etc/systemd/system/refeshDB.timer`

```
[Unit]
Description=Timer set to call refreshDB service

[Timer]
Unit=refreshDB.service
OnBootSec=30sec
OnUnitActiveSec=1min

[Install]
WantedBy=multi-user.target
```

**Start and enable the service**
> `sudo systemctl start refreshDB.timer`

> `sudo systemctl enable refreshDB.timer`
