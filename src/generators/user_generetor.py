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
    user = UserGenerator()
    print(user.last_name) 
    user.set_localizations('ru_RU')
    user.gen_first_name()
    user.gen_last_name()
    print(user.last_name)    
    print(user.get_object())
