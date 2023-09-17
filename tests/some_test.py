import requests

from configure import TESTED_URL
from src.base_clases.response import Response
from src.pydantic_schemas.base_schem import Company


def test_getting_post(get_post):
    respose = Response(get_post)
    respose.valisete_status_code(200)
    respose.validete_data(Company)