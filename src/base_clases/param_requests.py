import requests
from configure import TESTED_URL

class ApiRequests():
    def __init__(self, **kwarg) -> None:
        self.resurl = TESTED_URL
        self.timeout = 10
        self.params_req = {'None': None}
        self.headers = {'None': None}
        self.parameter_finilize = None
        self._parse_parameters(**kwarg)
        self.data = None
        self.json = None

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

            if par == 'data':
                self.headers = kwarg[par]

            if par == 'json':
                self.headers = kwarg[par]
                
            if par == 'parameter_finilize':
                self.headers = kwarg[par]

    def set_parameters(self, **kwarg):
        self._parse_parameters(**kwarg)

    def send_get(self):
        return requests.get(url=self.resurl, params=self.params_req,
                         headers=self.headers, timeout=self.timeout)
    
    def sed_delete(self):
        return requests.delete(url=self.resurl, params=self.params_req,
                         headers=self.headers, timeout=self.timeout)
    
    def sed_post(self):
        return requests.post(url=self.resurl, params=self.params_req,
                         headers=self.headers,data=self.data,json=self.json, timeout=self.timeout)
    def sed_put(self):
        return requests.put(url=self.resurl, params=self.params_req,
                         headers=self.headers,data=self.data,json=self.json, timeout=self.timeout)
    
    def finalise(self):
        if isinstance(self.parameter_finilize,dict):
            requests.delete(url=self.resurl,**self.parameter_finilize,timeout=self.timeout)    
    


if __name__ == '__main__':
    test_req = ApiRequests(api_path='users', params_req={'limit': 2, 'offset': 1})
    print(test_req.send_get())