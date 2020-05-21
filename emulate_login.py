from os import environ
from urllib.parse import urlparse, urlencode
from bs4 import BeautifulSoup

from settings import SSB_URL

LOGIN_TARGET_PATH = '/PROD/fhda_uportal.P_DeepLink_Post'
LOGIN_TARGET_URL = SSB_URL + LOGIN_TARGET_PATH + '?p_page=bwskcrse.P_CrseSchdDetl&p_payload=e30='

SSB_LOGIN_URL = SSB_URL + '/ssomanager/saml/login?' + urlencode({
    'relayState': '/c/auth/SSB?pkg=' + LOGIN_TARGET_URL
})

TRACE = False

def login(session):
    i = 0
    next_url = SSB_LOGIN_URL
    last_url = ''
    data = []

    while True:
        # Send a POST request to the next URL with specified data
        # TODO: Use GET instead of POST for SSB_LOGIN_URL; this seems to work for now
        res = session.post(next_url, data)
        res.raise_for_status()

        # Debug / trace logging
        if TRACE:
            print('POST to: ' + next_url + '\n')
            if next_url != res.url:
                print('Redirected to: ' + res.url + '\n')

        # Break if we have reached our target URL
        last_url = urlparse(res.url)
        if last_url.path == LOGIN_TARGET_PATH:
            break

        # Parse the HTML page for forms
        soup = BeautifulSoup(res.content, 'html5lib')
        form = soup.find('form')
        next_url = form.attrs['action']
        inputs = form.findAll('input')

        # Validate the existance of a <form> element
        if not form:
            print('[WARNING] Login - No form found on page! Exiting prematurely')
            break

        # Convert paths to URLs
        if next_url.startswith('/'):
            next_url = last_url.scheme + '://' + last_url.hostname + form.attrs['action']

        if i == 0:
            # On the first page, use the specified login data
            # TODO: gracefully exit with error message when environment variables are not present
            data = [
                ('j_username', environ['MP_USER']),
                ('j_password', environ['MP_PASS']),
                ('_eventId_proceed', ''),
            ]
        else:
            # Subsequent HTML pages have an autosubmitting <form>
            # Emulate auto-submission and use <input> element values for the data
            data = []
            for input_el in inputs:
                if input_el.has_attr('name') and input_el.has_attr('value'):
                    data.append((input_el.attrs['name'], input_el.attrs['value']))

        i += 1

    return session


if __name__ == '__main__':
    import requests

    TRACE = True

    my_session = requests.session()
    login(my_session)
    # print(my_session.cookies.get_dict())
