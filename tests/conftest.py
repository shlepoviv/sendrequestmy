import pytest

from src.base_clases.param_requests import ApiRequests

@pytest.fixture()
def get_post():
    req = ApiRequests()
    return req
