from base import BaseClient
import requests


class GettingID(BaseClient):
    v = 5.58
    user_id = None

    def __init__(self, username):
        super().__init__('https://api.vk.com/method/', 'users.get', 'GET')
        self.user_id = username

    def get_params(self):
        return {'user_ids': self.user_id, 'v': self.v}

    def _get_data(self, method, http_method):
        r = requests.get(self.generate_url(method), self.get_params())
        print(r.json())
        print(r.url)
        return r


