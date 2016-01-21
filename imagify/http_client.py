from .errors import raise_errors_on_failure
import requests
import json

class HttpClient(object):

    def validate_response(self, r):
        if r.status_code == requests.codes.ok or r.status_code == 422:
            return r.json()
        return raise_errors_on_failure(r)

    def post(self, endpoint, payload=False, files=False):
        if files:
            files = {'image': (open(files, 'rb'))}
        if payload:
            payload = {'data': json.dumps(payload)}
        r = requests.post(self.base_url + endpoint,
                          data=payload, files=files, headers=self.headers)
        return self.validate_response(r)

    def get(self, endpoint):
        r = requests.get(self.base_url + endpoint,
                         headers=self.headers)
        return self.validate_response(r)
