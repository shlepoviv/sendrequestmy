import requests

from configure import TESTED_URL
from src.schem import get_schem
from src.base_clases.response import Response


def test_getting_post():
    r = requests.get(url=TESTED_URL,timeout=10)
    respose = Response(r)
    respose.valisete_status_code(200)
    respose.validetejson(get_schem('companies'))


if __name__ == '__main__':
    test_getting_post()