from configure import TESTED_URL
from src.base_clases.response import Response
from src.pydantic_schemas.company import CompanyList


# Получить список компаний, проверить структуру объектов, проверить статус код.
# Проверить фильтрацию по статусу, действительно ли фильтруются данные.
# Проверить фильтрацию с использованием лимита и оффсета.

def test_getting_post(get_post):
    '''
    Get a list of companies, chek the obgect structure, chek status code
    Получить список компаний, проверить структуру объектов, проверить статус код.
    '''
    respose = Response(get_post)
    respose.valisete_status_code(200)
    respose.validete_data(CompanyList)