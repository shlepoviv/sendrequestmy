from typing import Union

from pydantic import BaseModel
from pydantic.types import List

class Meta(BaseModel):
    limit:int
    offset:int 
    total:int


class ValidationError(BaseModel):
    loc : List[Union[str,int]]
    msg: str
    type: str


class HTTPValidationError(BaseModel):
    detail:	List[ValidationError]