import json
import requests
import sys


class Auth:
    def __init__(self, _url, _user, _password):
        self.response = ""
        self.CSRF = ""
        self.return_data = ""
        self.auth_cookie = ""
        self._url = _url
        self._auth_url = _url + "access/ticket"
        self._connection = {"username": _user, "password": _password}
        self.connect()

    def connect(self):
        self.response = requests.post(self._auth_url, verify=False, data=self._connection)
        result = self.response

        if not self.response.ok:
            raise AssertionError('Login Failed: \n {} '.format(self.response))

        self.return_data = {'status': {'code': self.response.status_code,
                                       'ok': self.response.ok,
                                       'reason': self.response.reason}}
        self.return_data.update(result.json())

        self.auth_cookie = {'PVEAuthCookie': self.return_data['data']['ticket']}
        self.CSRF = self.return_data['data']['CSRFPreventionToken']

