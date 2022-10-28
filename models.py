from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    fullname: str
    hard_skills: List[str]
    soft_skills: List[str]
    character: List[str]

class UserSkills(BaseModel):
#    type: str
    list: List[str]