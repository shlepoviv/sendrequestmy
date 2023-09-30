from src.generators.base_generator import BaseGenerator


class UserGenerator(BaseGenerator):
    def __init__(self) -> None:
        super().__init__()
        self.last_name = None
        self.first_name = None
        self.gen_last_name()    

    def gen_last_name(self) -> None:
        self.last_name =  self._faker.last_name()

    def gen_first_name(self) -> None:
        self.first_name = self._faker.first_name()

if __name__ == '__main__':
    _user = UserGenerator()
    print(_user.last_name) 
    _user.set_localizations('ru_RU')
    _user.gen_first_name()
    _user.gen_last_name()
    print(_user.last_name)    
    print(_user.get_object())
