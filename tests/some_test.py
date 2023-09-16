import requests

from configure import TESTED_URL
from src.base_clases.response import Response
from src.pydantic_schemas.base_schem import Company


def test_getting_post():
    r = requests.get(url=TESTED_URL,timeout=10)
    respose = Response(r)
    respose.valisete_status_code(200)
    respose.validete_data(Company)

if __name__ == '__main__':
    test_getting_post()