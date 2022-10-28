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


class Project(BaseModel):
    title: str
    nedeed_hard: List[str]
    nedeed_soft: List[str]
    nedeed_character: List[str]
    compatibility_cup: int
    max_teammates: int
    memders: List[int]