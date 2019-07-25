
import os
from collections import namedtuple

from skills import Skill, Achievement
from utils import *

class Student:
    def __init__(self, login, name, avatar, achievements):
        self.login = login
        self.name = name
        self.avatar = avatar

        self.achievements = achievements

    def toJSON(self):
        return f'''
{{
    "login": "{self.login}",
    "name": "{self.name}",
    "avatar": "{self.avatar}"
}}'''

    @staticmethod
    def load(student_login):
        key = load_key(f'students/{student_login}.key')
        json_dict = load_from_file(f'students/{student_login}')
        json_dict = json.loads(json_dict)
        s = Student(json_dict['login'], json_dict['name'], json_dict['avatar'], [])

        if key:
            json_achievements = load_encrypted(f'students/{student_login}-achievements', key)
            json_achievements = json.loads(json_achievements)
            s.achievements = [Achievement(**ach) for ach in json_achievements]

        return s


    def compute_grade(self):
        total_xp = 0
        for ach in self.achievements:
            total_xp += ach.skill.xp

        # TODO: checar conceito final aqui!

        return total_xp

Team = namedtuple('Team', ['name', 'students', 'achievements'])



student_folder = os.path.dirname(__file__)
student_logins = [s[:-4] for s in os.listdir(student_folder) if s.endswith('.key')]

students = [Student.load(login) for login in student_logins]

#with open('students/teams-tutorial') as f:
#    all_teams = [
#        Team(**t) for t in json.load(f)
#    ]
