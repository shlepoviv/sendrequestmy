import pytest

from src.base_clases.param_requests import ApiRequests
from src.base_clases.response import Response

from src.generators.user_generetor import UserGenerator

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
    test_user = UserGenerator()
    test_user.gen_first_name() 
    data = test_user.get_object()
    req.set_parameters(data = data)   
    respose = Response(req.send_post())
    req.set_parameters(parameter_finilize = {'object_id':respose.find_in_respose_data('user_id')})
    request.addfinalizer(req.finalise)
    return respose.response_data 
