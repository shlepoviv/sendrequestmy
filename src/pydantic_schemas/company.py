from pydantic import BaseModel ,Field
from pydantic.types import List
from src.pydantic_schemas.service_data import Meta
from src.enums.company_enums import CompanyStatys
from src.enums.global_enums import TranslationLangsstring

class CompanyDescription(BaseModel):
    translation_lang:TranslationLangsstring
    translation: str = Field(default='')

class Company(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: CompanyStatys
    description_lang: List[CompanyDescription] = Field(default=None)




class CompanyList(BaseModel):
    data:List[Company]
    meta:Meta