from enum import Enum

class BaseEnum(Enum):
    @classmethod
    def return_all_count(cls):
        return [map(lambda v: v.value, cls)]

class GLOBAL_ERORR_MASSEGE(BaseEnum):
    WRONG_COdE= 'Wrong respose code'
    WRONG_ENUM_CONT = 'Count of enum difference of expected'

class TranslationLangsstring(BaseEnum):
    EN = 'EN'
    RU = 'RU'
    PL = 'PL'
    UA = 'UA'
