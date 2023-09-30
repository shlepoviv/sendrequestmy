from src.generators.base_generator import BaseGenerator


class CompanyGenerator(BaseGenerator):
    def __init__(self) -> None:
        super().__init__()
        self.id = None
        self.company_name = None
        self.gen_company_name()    

    def gen_company_name(self) -> None:
        self.company_name =  self._faker.company()


if __name__ == '__main__':
    com = CompanyGenerator()
    print(com.company_name) 
    com.set_localizations('ru_RU')
    com.gen_company_name()
    print(com.company_name)    
    print(com.get_object())