from openpyxl import *
import models


base = load_workbook('Users.xlsx')

base.active

users = base['Users']


def get_users(users):

    output = []

    i = 0

    j = 0

    fields = ['id','fullname','hard_skills','soft_skills','character']

    for row in users.rows:
        
        user = models.User
        
        data = {
            'id': '',
            'fullname': '',
            'hard_skills': '',
            'soft_skills': '',
            'character': ''
        }

        for cell in row:
            data[fields[j]] = cell.value
            j += 1
        
        output.append(data)
        j = 0
        i += 1
    
    base.close()

    return output

def register_user(user: models.User):

    rows = ['A','B','C','D','E']

    fields = ['id','fullname','hard_skills','soft_skills','character']

    j = 0

    position = users.max_row + 1

    for row in rows:
        users[f'{row}{position}'] = user[fields[j]]
        j += 1

    base.save('Users.xlsx')

pavlik = {
    'id': 12332,
    'fullname': 'Fuck Pasha',
    'hard_skills': "['Python','Html']",
    'soft_skills': "['Python','Html']",
    'character': "['Python','Html']"
}

register_user(pavlik)