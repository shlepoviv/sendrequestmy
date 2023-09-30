import pytest

from src.base_clases.param_requests import ApiRequests

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
