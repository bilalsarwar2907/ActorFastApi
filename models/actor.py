
from pydantic import BaseModel

from pydantic import BaseModel

class Actor(BaseModel):
    id: int
    name: str
    age: int
    gender: str 