import pytest

from src.pydantic_schemas.user import UsersList
from src.pydantic_schemas.service_data import HTTPValidationError

from src.base_clases.response import Response
from src.enums.company_enums import CompanyStatys
from src.enums.global_enums import TranslationLangsstring

pytestmark = pytest.mark.users

def test_getting_post_list_user(request_user):
    '''
    Get a list of users, chek the obgect structure, chek status code
    Получить список пользователей, проверить структуру объектов, проверить статус код.
    '''
    respose = Response(request_user.send_get())
    respose.valisete_status_code(200)
    respose.validete_data(UsersList)

@pytest.mark.parametrize ('limit,offset,exept',[
    (1,3,1),
    (1,1,1)])
def test_getting_post_list_users_with_limitoffet_filtr(limit,offset,exept,request_user):
    '''
    Chek the filter obgect with limit and offset
    Проверить фильтрацию с использованием лимита и оффсета.
    '''
    request_user.set_parameters(params_req ={'limit': limit,'offset': offset})
    respose = Response(request_user.send_get())
    respose.valisete_status_code(200)
    respose.validete_data(UsersList)
    assert len(respose.find_in_respose_data(['data'])) == exept
    assert respose.find_in_respose_data(['meta','limit']) == limit
    assert respose.find_in_respose_data(['meta','offset']) == offset
    