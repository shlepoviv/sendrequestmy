from typing import Union

from pydantic import BaseModel
from pydantic.types import List

class Meta(BaseModel):
    limit:int
    offset:int 
    total:int


class ValidationError(BaseModel):
    loc : List[Union[int, str]]
    msg: str
    title: str
    type: str


class HTTPValidationError(BaseModel):
    detail:	List[ValidationError]




