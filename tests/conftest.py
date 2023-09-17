import pytest
import requests
from configure import TESTED_URL

@pytest.fixture
def get_post():
    r = requests.get(url=TESTED_URL,timeout=10)
    return r