from src.schem import get_schem
from src.base_clases.response import Response


def test_getting_post(get_post):
    respose = Response(get_post)
    respose.valisete_status_code(200)
    respose.validetejson(get_schem('companies'))