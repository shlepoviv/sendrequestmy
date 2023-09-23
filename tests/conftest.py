import pytest
import requests
from configure import TESTED_URL

def _get_post(api_path,params=None):
    resurl=TESTED_URL
    if not isinstance(api_path,list):
        api_path = [api_path]
    for lvl in api_path:
        resurl = resurl + f'{lvl}/'      
    if not params:
        params = {'None':None}
    r = requests.get(url=resurl,params=params,timeout=10)
    return r

# companies/
@pytest.fixture()
def get_post():
    return _get_post