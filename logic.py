from typing import List
import models

def check_compatibility(user: models.User, project: models.Project):
    
    if user.id not in project.memders and project.max_teammates > len(project.memders):
        
        compatibility = 0
        
        for skill in user.hard_skills:
            if skill in project.nedeed_hard:
                compatibility+=1
        
        for skill in user.soft_skills:
            if skill in project.nedeed_soft:
                compatibility+=1

        for side in user.character:
            if side in project.nedeed_character:
                compatibility+=1

        if compatibility >= project.compatility_cup:
            project.memders.append(user.id)
            return True



def init_sort(user: models.User, projects: List[models.Project]):
    for project in projects:
        check_compatibility(user, project)