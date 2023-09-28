from faker import Faker

class BaseGenerator:
    def __init__(self) -> None:
        self._faker = Faker()

    def set_localizations(self, localizations:str = 'en_US') -> None:
        self._faker = Faker(localizations)

    def get_object(self) -> dict:
        return dict([(name_attr, self.__dict__[name_attr]) for name_attr in self.__dict__ if  (not name_attr.startswith('_')) and self.__dict__[name_attr]])
