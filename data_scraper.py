from urllib.request import urlopen
from os.path import abspath
import json

# 3rd party
import requests
from bs4 import BeautifulSoup

SCHEDULE = 'schedule.html'
TERM_CODE = '201841'


def main():
    # content = mine(write=True)
    content = urlopen(f'file://{abspath(SCHEDULE)}')
    parse(content)


def mine(write=False):
    headers = {
        'Origin': 'https://banssb.fhda.edu',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'FoothillAPI',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html, */*; q=0.01',
        'Referer': 'https://banssb.fhda.edu/PROD/fhda_opencourses.P_Application',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = [
      ('termcode', f'{TERM_CODE}'),
    ]

    res = requests.post('https://banssb.fhda.edu/PROD/fhda_opencourses.P_GetCourseList', headers=headers, data=data)
    res.raise_for_status()

    if write:
        with open(f'{SCHEDULE}', "wb") as file:
            for chunk in res.iter_content(chunk_size=512):
                if chunk:
                    file.write(chunk)

    return res.content


def parse(content):
    depts = list()

    soup = BeautifulSoup(content, 'html5lib')
    tables = soup.find_all('table', {'class': 'TblCourses'})

    for t in tables:
        d = Department(t['dept'], t['dept-desc'])

        rows = t.find_all('tr', {'class': 'CourseRow'})
        for r in rows:
            cols = r.find_all(lambda tag: tag.name == 'td' and not tag.get_text().isspace())
            for i, c in enumerate(cols):
                a = c.find('a')
                cols[i] = a.get_text() if a else cols[i].get_text()

            s = Section(cols)
            d.sections.append(s)

        depts.append(d)

    print(depts[0].__dict__)


class Section():
    def __init__(self, data):
        self.course, self.CRN, self.desc, self.status, self.days, self.time, self.start, self.end,\
            self.room, self.campus, self.units, self.instructor, self.seats, self.wait_seats, self.wait_cap = data


class Department():
    def __init__(self, dept, dept_desc):
        self.dept = dept
        self.dept_desc = dept_desc
        self.sections = list()


if __name__ == "__main__":
    main()

# Course | CRN | Title | Status | Days | Time | Start | End | | Room
# | Campus | Units | Instructor | Seats Available | Waitlist Slots | Waitlist Capacity |
