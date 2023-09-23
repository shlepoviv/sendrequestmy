import pytest
import requests
from configure import TESTED_URL
# companies/
@pytest.fixture()
def get_post_list_companies():
    r = requests.get(url=f'{TESTED_URL}companies/',timeout=10)
    return r