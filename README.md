# OwlAPI
This is an ~~unofficial~~ API that serves course data from MyPortal to students wishing to use it. If you have a suggestion for what other FHDA data this API should serve, drop an issue on Github. OwlAPI now has a home at [floof.li](https://floof.li).

#### Contributors
[**Kishan Emens**](https://github.com/phi-line), [Byron White](https://github.com/BoomSyrup), [Joshua Fan](https://github.com/joshuaptfan)

If you would like to contribute follow this [guide](https://github.com/FoothillCSClub/OwlAPI/blob/master/CONTRIBUTING.md).

#### Dependencies
[Quart](https://gitlab.com/pgjones/quart), [TinyDB](https://github.com/msiemens/tinydb), [Requests](https://github.com/requests/requests), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)


## Routes
### Get single
`GET /single` handles a single request to get a whole department or a whole course listing from the database
It expects a mandatory query parameter `dept` and an optionally `course`.

> `GET /single?dept=CS&course=2C`
```
{"40407":
  [
    {"CRN": "40407",
      "campus": "FH",
      "course": "C S F002C01Y",
      "days": "TTh",
      "desc": "ADV DATA  STRUCT/ALGRM IN C++",
      "end": "06/29/2018",
      "instructor": "Staff",
      "room": "5607",
      "seats": "31",
      "start": "04/09/2018",
      "status": "Open",
      "time": "01:30 PM-03:20 PM",
      "units": "  4.50",
      "wait_cap": "10",
      "wait_seats": "10"},
    {...}
  ]
}
```

<div id="interact"><div data-request-type="GET" data-request-url="/single" data-request-body="?dept=CS&course=2C"></div></div>

**Coming soon: filters**


### Get batch
`POST /batch` handles a batch request to get many departments or a many course listings from the database.
This batch request is meant to simulate hitting the api route with this data N times.
It expects a mandatory list of objects containing keys `dept` and `course`.

> `POST /batch`
```
{
  "courses": [
    {"dept":"CS", "course":"1A"},
    {"dept":"MATH", "course":"1A"},
    {"dept":"ENGL", "course":"1A"}
  ]
}
```

<div id="interact"><div data-request-type="POST" data-request-url="/batch" data-request-body='{"courses":[{"dept":"CS","course":"1A"},{"dept":"MATH","course":"1A"},{"dept":"ENGL","course":"1A"}],"filters":{"status":"Open", "types":{"standard":0, "online":1, "hybrid":0}, "days":{"M":1, "T":1, "W":1, "Th":1, "F":1, "S":0, "U":0}}}'></div></div>


### List
`GET /list` handles a single request to list department or course keys from the database
It takes an optional query parameter `dept` which is first checked for existence and then returns the dept keys.

> `GET /list`
```
IDS, CHLD, ALTW, ANTH, SPAN, CRWR, DH, NCLA, POLI, CHEM, CNSL, GIST, MTEC, ASTR, PHOT, ITRN, DMS, AHS, EMTP, ATHL, APEL, HIST, HORT, GEOG, SPED, ALCB, RT, MDIA, ENGR, THTR, NCSV, NCBS, ACTG, NCEL, KINS, DANC, HUMN, DA, JAPN, CRLP, VITI, BIOL, BUSI, PSE, _default, ECON, RSPT, ART, NCBH, PHT, LA, CS, LINC, MUS, EMS, PHED, ENGL, VT, HLTH, APPT, MATH, COMM, NCP, GID, LIBR, APSM, PHDA, PHIL, WMN, NANO, PSYC, ESLL, SOC, APIW, PHYS
```

> `GET /list?dept=CS`
```
2C, 49, 30A, 80A, 18, 21B, 50E, 3A, 22A, 50C, 50A, 20A, 2A, 1B, 1A, 81A, 53A, 82A, 30B, 63A, 21A, 53B, 1C, 2B, 10, 31A, 60A
```

<div id="interact"><div data-request-type="GET" data-request-url="/list" data-request-body="?dept=CS"></div></div>


### URLs
`GET /urls` returns a tree of all departments, their courses, and the courses' endpoints to hit.

> `GET /urls`
```
"CS":[
  {"10": "get?dept=CS&course=10",
  "18":  "get?dept=CS&course=18",
  "1A":  "get?dept=CS&course=1A",
  "1B":  "get?dept=CS&course=1B",
  "1C":  "get?dept=CS&course=1C",
  "20A": "get?dept=CS&course=20A",
  "21A": "get?dept=CS&course=21A",
  "21B": "get?dept=CS&course=21B",
  "22A": "get?dept=CS&course=22A",
  "2A":  "get?dept=CS&course=2A",
  "2B":  "get?dept=CS&course=2B",
  "2C":  "get?dept=CS&course=2C",
  "30A": "get?dept=CS&course=30A",
  "30B": "get?dept=CS&course=30B",
  {...}
],
"MATH": [...]
```

<div id="interact"><div data-request-type="GET" data-request-url="/urls" data-request-body=""></div></div>

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
#### OwlAPI service

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
