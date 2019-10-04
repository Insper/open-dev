
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
        json_dict = load_from_file(f'students/{student_login}')
        json_dict = json.loads(json_dict)
        s = Student(json_dict['login'], json_dict['name'], json_dict['avatar'], [])
        return s

    def load_skills(self):
        key = load_key(f'students/{self.login}.key')
        if key:
            json_achievements = load_encrypted(f'students/{self.login}-achievements', key)
            try:
                json_achievements = json.loads(json_achievements)
                for ach in json_achievements:
                    skill = all_skills[int(ach['skill_id'])]
                    metadata = ach['metadata']
                    self.achievements.append(Achievement(skill, metadata))
                    if 'shared_with' in metadata:
                        for login in metadata['shared_with']:
                            all_students[login].achievements.append(Achievement(skill, metadata))


            except json.JSONDecodeError:
                print(f'Arquivo students/{self.login}-achievements mal formatado!')
            self.has_key = True


    def compute_grade(self):
        total_xp = 0
        for ach in self.achievements:
            if 'shared_with' in ach.metadata:
                total_xp += ach.skill.xp / (len(ach.metadata['shared_with'])+1)
            else:
                total_xp += ach.skill.xp

        return total_xp
    

class Team:
    def __init__(self, name, students, achievements):
        self.name = name
        self.students = [all_students[st] for st in students]
        for st in students:
            for ach in achievements:
                skill = all_skills[int(ach['skill_id'])]
                metadata = ach['metadata']
                all_students[st].achievements.append(Achievement(skill, metadata))
                
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

[s.load_skills() for s in all_students.values()]

all_teams = [Team.load(t[5:]) for t in os.listdir(student_folder) if t.startswith('team-')]
