from enum import Enum
from pydantic import BaseModel

# Enumeration
class CompanyStatys(str, Enum):
    ACTIVE = "ACTIVE"
    BANKRUPT = "BANKRUPT"
    CLOSED = "CLOSED"        
# End Enumeration

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