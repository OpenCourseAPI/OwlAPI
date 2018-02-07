from urllib.request import urlopen
from os.path import abspath
from collections import defaultdict

# 3rd party
import requests
from bs4 import BeautifulSoup

SCHEDULE = 'schedule.html'


def main():
    # content = mine()
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
        'Referer': 'https://banssb.fhda.edu/PROD/fhda_opencourses.P_Application?portaldef=201841',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = [
      ('termcode', '201841'),
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
    listings = defaultdict(list)

    soup = BeautifulSoup(content, 'html5lib')
    tables = soup.find_all('table', {'class': 'TblCourses'})

    for t in tables:
        rows = t.find_all('tr', {'class': 'CourseRow'})
        listings[t['dept-desc']].append(rows)

    print(listings['Accounting'])


if __name__ == "__main__":
    main()
