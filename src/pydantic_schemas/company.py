from pydantic import BaseModel ,Field
from pydantic.types import List
from src.pydantic_schemas.service_data import Meta
from src.enums.company_enums import CompanyStatys
from src.enums.global_enums import TranslationLangsstring

class CompanyDescription(BaseModel):
    translation_lang:TranslationLangsstring
    translation: str

class Company(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: CompanyStatys
    description_lang: CompanyDescription = Field(default=None)
    description: str = Field(default='')



class CompanyList(BaseModel):
    data:List[Company]
    meta:Meta