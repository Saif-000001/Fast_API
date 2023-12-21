from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "Male"
    female = "Femal"
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):

    first_name:str
    middle_name:Optional[str]
    last_name: str
    gender:Gender
    roles:List[Role]