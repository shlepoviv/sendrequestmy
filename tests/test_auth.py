import pytest

from src.pydantic_schemas.service_data import HTTPValidationError
from src.pydantic_schemas.user import TokenResponse

from src.base_clases.response import Response

from src.generators.login_password_generator import LoginPasswordGenerator

from configure import PASSWORD_AUTH

@pytest.mark.parametrize('param,val',
                         [('timeout',360),
                          ('timeout',10),
                          ('timeout',None)])
def test_successful_auth(request_auth,param,val):
    '''
    Check successful authorization
    Проверка успешной авторизации
    '''
    data = LoginPasswordGenerator().get_object()
    data['password'] = PASSWORD_AUTH
    if val:
        data['param'] = val
    else:
        if not data.get(param,'non_expec') == 'non_expec': data.pop(param) 
    request_auth.set_parameters(data = data)
    respose = Response(request_auth.send_post())
    respose.valisete_status_code(200)
    respose.validete_data(TokenResponse)


@pytest.mark.parametrize('param,val',
                         [('password',None),
                          ('password',1),
                          ('timeout','a'),
                          ('login','a'),
                          ('login',None),])
def test_unsuccessful_auth(request_auth,param,val):
    '''
    Check unsuccessful authorization
    Проверка неудачной авторизации
    '''
    data = LoginPasswordGenerator().get_object()
    data['password'] = PASSWORD_AUTH
    if val:
        data[param] = val
    else:
        if not data.get(param,'non_expec') == 'non_expec': data.pop(param) 
    print(data)
    request_auth.set_parameters(data = data)
    respose = Response(request_auth.send_post())
    respose.valisete_status_code([403, 404, 422])
    if respose.status_code == 422:
        respose.validete_data(HTTPValidationError)
