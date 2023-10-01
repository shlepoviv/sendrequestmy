from datetime import datetime
from typing import Optional


from pydantic import BaseModel,Field, EmailStr 
from pydantic.types import List

from src.pydantic_schemas.service_data import Meta

class BaseUser(BaseModel):
    first_name: str
    last_name: str
    company_id: int 

class TokenResponse(BaseModel):
    token: str

class ResponseUser(BaseModel):
    first_name: Optional[str] = Field(default = None)
    last_name: str 
    company_id: Optional[int] = Field(default = None)
    user_id: int

class MeResponse(BaseModel):
    token: Optional[str] = Field(default = None)
    user_name: str
    email_address:	EmailStr 
    valid_till:	datetime


class UsersList(BaseModel):
    meta: Meta
    data: List[ResponseUser]

class UserCredentials(BaseModel):
    login: str = Field(ge = 3)
    password: str
    timeout: int = Field(default= 360)
 
