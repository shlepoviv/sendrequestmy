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

@pytest.mark.parametrize ('last_name,company_id',[
    (True,None),
    (False,100500)
    ]
    )

def test_negative_create_user(last_name,company_id,request_user):
    '''
    Check create user
    Проверить создание пользователя
    '''
    user = UserGenerator()
    if last_name:
        user.gen_first_name() 
        user.last_name = None
    data = user.get_object()
    if company_id:
        data['company_id'] = company_id
    request_user.set_parameters(data = data)
    respose = Response(request_user.send_post())
    respose.valisete_status_code([404, 422])
    if respose.status_code == 422:
        respose.validete_data(HTTPValidationError)



def test_getting_post_user(request_user,test_user):
    '''
    Get user, chek the obgect structure, chek status code
    Получить пользователя, проверить структуру объектов, проверить статус код.
    '''
    request_user.set_parameters(object_id = test_user['user_id'])
    respose = Response(request_user.send_get())
    respose.valisete_status_code(200)
    respose.validete_data(ResponseUser)


def test_getting_non_existent_user(request_user,test_user):
    '''
    Get non existent user, chek the obgect structure, chek status code
    Получить несуществующего пользователя, проверить структуру объектов, проверить статус код.
    '''
    request_user.set_parameters(object_id = (test_user['user_id']+100))
    respose = Response(request_user.send_get())
    respose.valisete_status_code([404, 422])
    if respose.status_code == 422:
        respose.validete_data(HTTPValidationError)


def test_change_user(request_user,test_user,active_company):
    '''
    Change user, chek the obgect structure, chek status code
    Изменить пользователя, проверить структуру объектов, проверить статус код.
    '''
    test_user['first_name'] = None
    test_user['company_id'] = active_company['company_id']
    request_user.set_parameters(object_id = test_user.pop('user_id'),data = test_user)
    respose = Response(request_user.send_put())
    respose.valisete_status_code(200)
    respose.validete_data(ResponseUser)
    assert respose.find_in_respose_data('first_name') == None
    assert respose.find_in_respose_data('company_id') == active_company['company_id']

@pytest.mark.parametrize('par,val',
                         [('company_id',100500),
                          ('company_id','closed_company'),
                          ('last_name', None)])
def test_negative_change_user(par,val,request_user,test_user,closed_company):
    '''
    Change user, chek the obgect structure, chek status code
    Изменить пользователя, проверить структуру объектов, проверить статус код.
    '''
    test_user[par] = val if val !='closed_company' else closed_company
    request_user.set_parameters(object_id = test_user.pop('user_id'),data = test_user)
    respose = Response(request_user.send_put())
    respose.valisete_status_code([404, 422])
    if respose.status_code == 422:
        respose.validete_data(HTTPValidationError)

def test_delete_user(request_user,test_user):
    '''
    Delete user, chek status code
    Удалить пользователя, проверить статус код.
    '''
    request_user.set_parameters(object_id = test_user.pop('user_id'))
    respose = Response(request_user.send_delete())
    respose.valisete_status_code(202)

def test_negative_delete_user(request_user,test_user):
    '''
    Delete non existing non user, chek status code
    Удалить несуществующего пользователя, проверить статус код.
    '''
    request_user.set_parameters(object_id = (test_user.pop('user_id')+100))
    respose = Response(request_user.send_delete())
    respose.valisete_status_code([404, 422])
    if respose.status_code == 422:
        respose.validete_data(HTTPValidationError)