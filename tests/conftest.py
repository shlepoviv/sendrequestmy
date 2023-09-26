import pytest
import requests
from configure import TESTED_URL

def _get_post(api_path,object_id = None,params_req=None,headers = None):
    resurl=TESTED_URL
    if not isinstance(api_path,list):
        api_path = [api_path]
    for lvl in api_path:
        resurl = resurl + f'{lvl}/' 
    if  object_id:      
        resurl = resurl + f'{object_id}' 
    if not params_req:
        params_req = {'None':None}
    if not headers:
        headers = {'None':None}
        
    r = requests.get(url=resurl,params=params_req,headers=headers,timeout=10)
    return r

# companies/
@pytest.fixture()
def get_post():
    return _get_post

_get_post('companies',object_id = 'f',headers ={'Accept-Language': 'Pu'})