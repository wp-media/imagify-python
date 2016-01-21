from .http_client import HttpClient
from .errors import ImagifyError


class Imagify(object):
    __version__ = "0.0.1"

    def __init__(self, api_key=False):
        if not api_key:
            raise ImagifyError('You have to specify your API Key')
        self.api_key = api_key
        self.http_client = HttpClient()
        self.http_client.headers = {
            'Authorization': 'token {0}'.format(self.api_key)}
        self.base_url = self.http_client.base_url = 'https://app.imagify.io/api'

    def upload(self, files, param=False):
        """
        Upload method to optimize images
        """

        return self.http_client.post('/upload/', files=files, payload=param)

    def version(self):
        req = self.http_client.get('/version/')
        return req["version"]
