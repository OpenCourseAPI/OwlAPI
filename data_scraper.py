from bs4 import BeautifulSoup
import requests

headers = {
    'Origin': 'https://banssb.fhda.edu',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
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

with open('schedule.html', "wb") as file:
    for chunk in res.iter_content(chunk_size=512):
        if chunk:
            file.write(chunk)

# content = res.content
# soup = BeautifulSoup(content, 'html5lib')
