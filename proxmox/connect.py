import requests


class Connect:
    def __init__(self, _auth):
        self.returned_json = ""
        self.auth = _auth

        self.url = ""
        self.auth_token = ""
        self.CSRF = ""
        self.response = ""
        self.get_auth()


    def get_auth(self):
        self.url = self.auth._url
        self.auth_token = self.auth.auth_cookie
        self.CSRF = self.auth.CSRF


    def connect(self, option):
        requests.packages.urllib3.disable_warnings()

        api_url = "%s%s" % (self.url, option)

        self.response = requests.get(api_url, verify=False, cookies=self.auth_token)

        try:
            self.returned_json = self.response.json()
            self.returned_json.update({'status': {'code': self.response.status_code,
                                                  'ok': self.response.ok,
                                                  'reason': self.response.reason}})
            return self.returned_json
        except:
            print("Error in trying to process JSON")
            print(self.response)