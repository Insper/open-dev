
import os
from collections import namedtuple

from skills import Skill, Achievement, all_skills
from utils import *

class Student:
    def __init__(self, login, name, avatar, achievements):
        self.login = login
        self.name = name
        self.avatar = avatar
        self.has_key = False

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
            try:
                json_achievements = json.loads(json_achievements)
                for ach in json_achievements:
                    skill = all_skills[int(ach['skill_id'])]
                    metadata = ach['metadata']
                    s.achievements.append(Achievement(skill, metadata, s))

            except json.JSONDecodeError:
                print(f'Arquivo students/{student_login}-achievements mal formatado!')
            s.has_key = True

        return s

    def compute_grade(self):
        total_xp = 0
        for ach in self.achievements:
            if ach.user != self:
                print('Skill:', str(ach.skill), 'xp:', ach.xp(), 'origem:', str(ach.user))
            else:
                print('Skill:', str(ach.skill), 'xp:', ach.xp())
            total_xp += ach.xp()
            
        return total_xp
    

class Team:
    def __init__(self, name, students, achievements):
        self.name = name
        self.students = [all_students[st] for st in students]
        for st in students:
            for ach in achievements:
                skill = all_skills[int(ach['skill_id'])]
                metadata = ach['metadata']
                all_students[st].achievements.append(Achievement(skill, metadata, st))

        self.achievements = achievements
    
    @staticmethod
    def load(fname):
        with open(f'students/team-{fname}') as f:
            vals = json.load(f)
        return Team(**vals)

    def toJSON(self):
        student_logins = json.dumps([st.login for st in self.students])
        json_achievements = json.dumps(self.achievements)
        return f'''
{{
    "name": "{self.name}",
    "students": {student_logins},
    "achievements": {json_achievements}
}}'''

student_folder = os.path.dirname(__file__)
student_logins = [s.split('-')[0] for s in os.listdir(student_folder) if s.endswith('-achievements')]

all_students = {login:Student.load(login) for login in student_logins}

all_teams = [Team.load(t[5:]) for t in os.listdir(student_folder) if t.startswith('team-')]
