
import os
from collections import namedtuple
import itertools

from skills import Skill, Achievement, all_skills
from utils import *

class Student:
    def __init__(self, login, name, ghuser, achievements):
        self.login = login
        self.name = name
        self.ghuser = ghuser
        self.avatar = get_gh_picture(ghuser)
        self.has_key = False

        self.achievements = achievements

    def __str__(self):
        return self.name

    def toJSON(self):
        return f'''
{{
    "login": "{self.login}",
    "name": "{self.name}",
    "ghuser": "{self.ghuser}"
}}'''

    @staticmethod
    def load(student_login):
        json_dict = load_from_file(f'students/{student_login}')
        json_dict = json.loads(json_dict)
        s = Student(json_dict['login'], json_dict['name'], json_dict.get('ghuser', ''), {})
        return s

    @property
    def all_achievements(self):
        return itertools.chain(*self.achievements.values())

    def _add_achievement(self, ach):
        if not ach.skill.id in self.achievements:
            self.achievements[ach.skill.id] = []

        self.achievements[ach.skill.id].append(ach)

    def _load_skills_from_string(self, filename):
        json_achievements = json.loads(filename)
        for ach in json_achievements:
            skill_id = all_skills[int(ach['skill_id'])]
            metadata = ach['metadata']

            self._add_achievement(Achievement(skill_id, metadata, self))

            if 'group' in metadata:
                for login in metadata['group']:
                    try:
                        all_students[login]._add_achievement(Achievement(skill_id, metadata, self))
                    except KeyError:
                        print(f'Arquivo students/{self.login}-achievements mal formatado!')
            

    def load_skills(self):
        key = load_key(f'students/{self.login}.key')
        if key:
            json_achievements = load_encrypted(f'students/{self.login}-achievements', key)
            try:
                self._load_skills_from_string(json_achievements)
            except json.JSONDecodeError:
                print(f'Arquivo students/{self.login}-achievements mal formatado!')
            self.has_key = True

    def compute_grade(self):
        total_xp = 0
        for ach in self.all_achievements:
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
    

student_folder = os.path.dirname(__file__)
student_logins = [s.split('-')[0] for s in os.listdir(student_folder) if s.endswith('-achievements')]

all_students = {login:Student.load(login) for login in student_logins}
project_points = {login: 0 for login in student_logins}

[s.load_skills() for s in all_students.values()]
