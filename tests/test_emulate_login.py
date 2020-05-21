from os import environ
from unittest import TestCase
from requests import session

from emulate_login import login

class TestLogin(TestCase):
    def test_login_works(self):
        if not (environ.get('MP_USER') and environ.get('MP_PASS')):
            return

        login_session = session()
        login(login_session)
        cookies = login_session.cookies.get_dict()

        # TODO: improve methodology to test login
        self.assertGreater(len(cookies), 1)
