
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

    def __str__(self):
        return self.name

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
                    self.achievements.append(Achievement(skill, metadata, self))
                    if 'shared_with' in metadata:
                        for login in metadata['shared_with']:
                            try:
                                all_students[login].achievements.append(Achievement(skill, metadata, self))
                            except KeyError:
                                print(f'Arquivo students/{self.login}-achievements mal formatado!')
                    if type(metadata) == dict and 'project' in metadata:
                        group_size = len(metadata['project']) 
                        for login in metadata['project']:
                            try:
                                project_points[login] += self.achievements[-1].xp() / group_size
                            except KeyError:
                                print(f'Arquivo students/{self.login}-achievements mal formatado!')

                    if type(metadata) == dict and 'copy_to' in metadata:
                        for login in metadata['copy_to']:
                            try:
                                all_students[login].achievements.append(Achievement(skill, metadata, self))
                            except KeyError:
                                print(f'Arquivo students/{self.login}-achievements mal formatado!')

            except json.JSONDecodeError:
                print(f'Arquivo students/{self.login}-achievements mal formatado!')
            self.has_key = True

    def compute_grade(self):
        total_xp = 0
        for ach in self.achievements:
            if 'shared_with' in ach.metadata:
                xp_achi = ach.xp() / (len(ach.metadata['shared_with'])+1)
            else:
                xp_achi = ach.xp()

            if ach.user != self:
                print('Skill:', str(ach.skill), 'xp:', xp_achi, 'origem:', str(ach.user))
            else:
                print('Skill:', str(ach.skill), 'xp:', xp_achi)
            total_xp += xp_achi
            
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
project_points = {login: 0 for login in student_logins}

[s.load_skills() for s in all_students.values()]
all_teams = [Team.load(t[5:]) for t in os.listdir(student_folder) if t.startswith('team-')]
