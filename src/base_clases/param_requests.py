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
                self.data = kwarg[par]
                
            if par == 'parameter_finilize':
                self.parameter_finilize = kwarg[par]

    def set_parameters(self, **kwarg):
        self._parse_parameters(**kwarg)

    def send_get(self):
        return requests.get(url=self.resurl, params=self.params_req,
                         headers=self.headers, timeout=self.timeout)
    
    def send_delete(self):
        return requests.delete(url=self.resurl, params=self.params_req,
                         headers=self.headers, timeout=self.timeout)
    
    def send_post(self):
        return requests.post(url=self.resurl, params=self.params_req,
                         headers=self.headers,json=self.data, timeout=self.timeout)
    def send_put(self):
        return requests.put(url=self.resurl, params=self.params_req,
                         headers=self.headers,json=self.data, timeout=self.timeout)
    
    def finalise(self):
        if isinstance(self.parameter_finilize,dict):
            self._parse_parameters(**self.parameter_finilize)
            self.send_delete()   
    


if __name__ == '__main__':

    pass

