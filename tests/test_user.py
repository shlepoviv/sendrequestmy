import pytest

from src.pydantic_schemas.user import UsersList, ResponseUser
from src.pydantic_schemas.service_data import HTTPValidationError

from src.base_clases.response import Response
from src.generators.user_generetor import UserGenerator

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

@pytest.mark.parametrize ('company_id',[
    None,
    1
    ])
@pytest.mark.parametrize ('localaze',[
    ['ru_RU',
     'en_US']
    ])
@pytest.mark.parametrize ('first_name',[
    False,
    True
    ]
    )
def test_create_user(company_id,localaze,first_name,request_user):
    '''
    Check create user
    Проверить создание пользователя
    '''
    user = UserGenerator()
    user.set_localizations(localaze)
    if first_name:
        user.gen_first_name() 
    data = user.get_object()
    if company_id:
        data['company_id'] = company_id
    request_user.set_parameters(data = data)
    respose = Response(request_user.send_post())
    respose.valisete_status_code(201)
    respose.validete_data(ResponseUser)
    request_user.set_parameters(parameter_finilize = {'object_id':respose.find_in_respose_data('user_id')})
    