from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    fullname: str
    hard_skills: List[str]
    soft_skills: List[str]
    character: List[str]

external_data = {'id': 1,
                 'fullname': 'Suka Yeba',
                 'hard_skills': ['Python','HTML'],
                 'soft_skills': ['Communicative'],
                 'character': ['Sexy', 'Stylish']   
}

new_user = User(**external_data)

print(new_user.hard_skills[1])