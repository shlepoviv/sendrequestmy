from pydantic import BaseModel
from src.enums.company_enums import CompanyStatys

class Meta(BaseModel):
    limit:int
    offset:int 
    total:int
    
class Company(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: CompanyStatys

class PostCompany(BaseModel):
    data:list[Company]
    meta:Meta