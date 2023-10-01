from src.generators.base_generator import BaseGenerator


class LoginPasswordGenerator(BaseGenerator):
    def __init__(self) -> None:
        super().__init__()
        self.login = None
        self.password = None
        self.gen_login()   
        self.gen_password() 

    def gen_login(self) -> None:
        self.login = self._faker.user_name()

    def gen_password(self) -> None:
        self.password = self._faker.password()

if __name__ == '__main__':
    _par = LoginPasswordGenerator()
    print(_par.get_object()) 
    _par.set_localizations('ru_RU')
    _par.gen_login()
    _par.gen_password()
    print(_par.get_object())    
