# Setup
### Local setup

**Install pipenv**
> `pip3 install pipenv`


**Download all dependencies for OwlAPI**
> `pipenv install`


**Start pipenv session**
> `pipenv shell`


**Run Data Scraper**
> `python scrape_term.py`


**Start API Server**
> `python server.py`


### Server setup
This is a setup guide for using [`systemctl`](https://www.freedesktop.org/software/systemd/man/systemctl.html) to run the server in the background. This small guide also covers how to setup a servive to refresh the database on timed interval.

#### OwlAPI service
This service is the main driver which runs the API. Gunicorn is used to serve Python through [`WSGI`](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), and [`nginx`](https://www.nginx.com/) is used to direct port traffic to The API.

**Create a file named OwlAPI.service**
> `sudo vi /etc/systemd/system/OwlAPI.service`

**Paste in this sample config changing `user`**
```ini
[Unit]
Description=Gunicorn instance to serve OwlAPI
After=network.target

[Service]
User=user
Group=nginx
WorkingDirectory=/home/user/OwlAPI
Environment="PATH=/home/user/.local/share/virtualenvs/OwlAPI-mya9jbVn/bin/"
ExecStart=/home/user/.local/share/virtualenvs/OwlAPI-mya9jbVn/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 -m 007 server:application

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
```ini
[Unit]
Description=Timer job to refresh OwlAPI database
After=network.target

[Service]
User=user
Type=simple
WorkingDirectory=/home/user/OwlAPI
Environment=PATH=/home/user/.local/share/virtualenvs/OwlAPI-mya9jbVn/bin/
ExecStart=/home/user/.local/share/virtualenvs/OwlAPI-mya9jbVn/bin/python3.6 /home/user/OwlAPI/scrape_term.py
StandardError=journal

[Install]
WantedBy=multi-user.target
```

**Create a file named refeshDB.timer**
> `sudo vi /etc/systemd/system/refeshDB.timer`

```ini
[Unit]
Description=Timer set to call refreshDB service

[Timer]
Unit=refreshDB.service
OnBootSec=30sec
OnUnitActiveSec=2min

[Install]
WantedBy=multi-user.target
```

**Start and enable the service**
> `sudo systemctl start refreshDB.timer`

> `sudo systemctl enable refreshDB.timer`
