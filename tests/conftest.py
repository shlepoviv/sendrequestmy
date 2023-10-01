from time import sleep
import pytest

from src.base_clases.param_requests import ApiRequests
from src.base_clases.response import Response

from src.generators.user_generetor import UserGenerator
from src.generators.login_password_generator import LoginPasswordGenerator

from src.enums.company_enums import CompanyStatys

from configure import PASSWORD_AUTH

@pytest.fixture()
def request_company():
    req = ApiRequests(api_path='companies')
    return req

@pytest.fixture()
def request_user():
    req = ApiRequests(api_path='users')
    yield req
    if req.parameter_finilize:
        req.finalise()

@pytest.fixture()
def test_user(request):
    req = ApiRequests(api_path='users')
    t_user = UserGenerator()
    t_user.gen_first_name() 
    data = t_user.get_object()
    req.set_parameters(data = data)   
    respose = Response(req.send_post())
    req.set_parameters(parameter_finilize = {'object_id':respose.find_in_respose_data('user_id')})
    request.addfinalizer(req.finalise)
    return respose.response_data 

@pytest.fixture()
def active_company():
    req = ApiRequests(api_path='companies')
    req.set_parameters(params_req={'status': CompanyStatys.ACTIVE.value,'limit': 1, 'offset': 0})
    respose = Response(req.send_get())
    return respose.response_data['data'][0]

@pytest.fixture()
def closed_company():
    req = ApiRequests(api_path='companies')
    req.set_parameters(params_req={'status': CompanyStatys.CLOSED.value,'limit': 1, 'offset': 0})
    respose = Response(req.send_get())
    return respose.response_data['data'][0]


@pytest.fixture()
def request_auth():
    req = ApiRequests(api_path=['auth','authorize'])
    return req

@pytest.fixture()
def request_auth_with_token():
    req = ApiRequests(api_path=['auth'],object_id ='me')
    return req

@pytest.fixture()
def valide_token():
    req = ApiRequests(api_path=['auth','authorize'])
    data = LoginPasswordGenerator().get_object()
    data['password'] = PASSWORD_AUTH
    req.set_parameters(data = data)
    respose = Response(req.send_post())
    return respose.response_data['token']

@pytest.fixture()
def expired_token():
    req = ApiRequests(api_path=['auth','authorize'])
    data = LoginPasswordGenerator().get_object()
    data['password'] = PASSWORD_AUTH
    data['timeout'] = 1
    req.set_parameters(data = data)
    respose = Response(req.send_post())
    sleep(1)
    return respose.response_data['token']