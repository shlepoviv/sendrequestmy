import pytest

from src.base_clases.param_requests import ApiRequests

@pytest.fixture()
def get_post_company():
    req = ApiRequests(api_path='companies')
    return req

@pytest.fixture()
def get_post_user():
    req = ApiRequests(api_path='users')
    return req