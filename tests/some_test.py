import pytest

from src.pydantic_schemas.company import CompanyList

from src.base_clases.response import Response
from src.enums.company_enums import CompanyStatys


def test_getting_post_list_companies(get_post):
    '''
    Get a list of companies, chek the obgect structure, chek status code
    Получить список компаний, проверить структуру объектов, проверить статус код.
    '''
    respose = Response(get_post('companies'))
    respose.valisete_status_code(200)
    respose.validete_data(CompanyList)

@pytest.mark.parametrize ('status',CompanyStatys.return_all_count())
def test_getting_post_list_companies_with_status_filtr(status,get_post):
    '''
    Get a list of companies, chek the obgect structure, chek status code
    Получить список компаний, проверить структуру объектов, проверить статус код.
    '''
    respose = Response(get_post('companies',{'status': status}))
    respose.valisete_status_code(200)
    respose.validete_data(CompanyList)
    for i in respose.find_in_respose_data(['data']):
        assert i['company_status'] == status

@pytest.mark.parametrize ('limit,offset,exept',[
    (1,3,1),
    (1,1,1)])
def test_getting_post_list_companies_with_limitoffet_filtr(limit,offset,exept,get_post):
    '''
    Chek the filter obgect with limit and offset
    Проверить фильтрацию с использованием лимита и оффсета.
    '''
    respose = Response(get_post('companies',{'limit': limit,'offset': offset}))
    respose.valisete_status_code(200)
    respose.validete_data(CompanyList)
    assert len(respose.find_in_respose_data(['data'])) == exept
    assert respose.find_in_respose_data(['meta','limit']) == limit
    assert respose.find_in_respose_data(['meta','offset']) == offset