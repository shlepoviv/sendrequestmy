from typing import Union

from pydantic import BaseModel
from pydantic.types import List

class Meta(BaseModel):
    limit:int
    offset:int 
    total:int


class ValidationError(BaseModel):
    loc : List[str]
    # loc : List[Union[str,int]]
    msg: str
  #  title: str
    type: str


class HTTPValidationError(BaseModel):
    detail:	List[ValidationError]

ValidationError.validete_data("loc":["path","company_id"],"msg":"value is not a valid integer","type":"type_error.integer")


