import pytest

from src.pydantic_schemas.company import CompanyList, Company
from src.pydantic_schemas.service_data import HTTPValidationError

from src.base_clases.response import Response
from src.enums.company_enums import CompanyStatys
from src.enums.global_enums import TranslationLangsstring

pytestmark = pytest.mark.companies


def test_getting_post_list_companies(get_post_company):
    '''
    Get a list of companies, chek the obgect structure, chek status code
    Получить список компаний, проверить структуру объектов, проверить статус код.
    '''
    respose = Response(get_post_company.get_post())
    respose.valisete_status_code(200)
    respose.validete_data(CompanyList)


@pytest.mark.parametrize('status', CompanyStatys.return_all_count())
def test_getting_post_list_companies_with_status_filtr(status, get_post_company):
    '''
    Get a list of companies, chek the obgect structure, chek status code
    Получить список компаний, проверить структуру объектов, проверить статус код.
    '''
    get_post_company.set_parameters(params_req={'status': status})

    respose = Response(get_post_company.get_post())
    respose.valisete_status_code(200)
    respose.validete_data(CompanyList)
    for i in respose.find_in_respose_data(['data']):
        assert i['company_status'] == status


@pytest.mark.parametrize('limit,offset,exept', [
    (1, 3, 1),
    (1, 1, 1)])
def test_getting_post_list_companies_with_limitoffet_filtr(limit, offset, exept, get_post_company):
    '''
    Chek the filter obgect with limit and offset
    Проверить фильтрацию с использованием лимита и оффсета.
    '''
    get_post_company.set_parameters(
        params_req={'limit': limit, 'offset': offset})

    respose = Response(get_post_company.get_post())
    respose.valisete_status_code(200)
    respose.validete_data(CompanyList)
    assert len(respose.find_in_respose_data(['data'])) == exept
    assert respose.find_in_respose_data(['meta', 'limit']) == limit
    assert respose.find_in_respose_data(['meta', 'offset']) == offset


# Структуру компании и статус код.
# Делаем запрос с Accept-Language хедером, передав доступную локализацию. (Учитывайте негативные кейсы)
# Проверяем запрос по несуществующей компании.

def test_getting_post_company(get_post_company):
    '''
    Chek the copmany structure, chek status code
    '''
    get_post_company.set_parameters(object_id=1)
    respose = Response(get_post_company.get_post())
    respose.valisete_status_code(200)
    respose.validete_data(Company)


@pytest.mark.parametrize('header', [{'Accept-Language': lang} for lang in TranslationLangsstring.return_all_count()],
                         ids=TranslationLangsstring.return_all_count())
def test_getting_post_company_with_Accept_laguage(header, get_post_company):
    '''
    Chek the copmany structure, chek status code
    '''
    get_post_company.set_parameters(object_id=1, headers=header)

    respose = Response(get_post_company.get_post())
    respose.valisete_status_code(200)
    respose.validete_data(Company)


@pytest.mark.parametrize('object_id', ['a', 100500])
def test_getting_bed_post_company(object_id, get_post_company):
    '''
    Chek the get with bed id company, chek status code
    '''
    get_post_company.set_parameters(object_id=object_id)

    respose = Response(get_post_company.get_post())
    respose.valisete_status_code([404, 422])
    if respose.status_code == 422:
        respose.validete_data(HTTPValidationError)
