import requests

from configure import TESTED_URL
from src.schem import get_schem
from src.base_clases.response import Response
from src.pydantic_schemas.base_schem import PostCompany


def test_getting_post():
    r = requests.get(url=TESTED_URL,timeout=10)
    respose = Response(r)
    respose.valisete_status_code(200)
    respose.validetejson(get_schem('companies'))
    post_com = PostCompany.model_validate(r.json())
    print(post_com)

if __name__ == '__main__':
    test_getting_post()