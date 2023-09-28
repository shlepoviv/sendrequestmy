import requests
from configure import TESTED_URL

class ApiRequests():
    def __init__(self, **kwarg) -> None:
        self.resurl = TESTED_URL
        self.timeout = 10
        self.params_req = {'None': None}
        self.headers = {'None': None}
        self._parse_parameters(**kwarg)

    def _parse_parameters(self, **kwarg) -> None:
        for par in kwarg:
            if par == 'api_path':
                api_path = kwarg[par]
                if not isinstance(api_path, list):
                    api_path = [api_path]
                for lvl in api_path:
                    self.resurl = self.resurl + f'{lvl}/'

            if par == 'object_id':
                self.resurl = self.resurl + f'{kwarg[par]}'

            if par == 'params_req':
                self.params_req = kwarg[par]

            if par == 'headers':
                self.headers = kwarg[par]

    def set_parameters(self, **kwarg):
        self._parse_parameters(**kwarg)

    def get_post(self):


        return requests.get(url=self.resurl, params=self.params_req,
                         headers=self.headers, timeout=self.timeout)


if __name__ == '__main__':
    test_req = ApiRequests(api_path='users', params_req={'limit': 2, 'offset': 1})
    print(test_req.get_post())