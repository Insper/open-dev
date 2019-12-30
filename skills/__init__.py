
from collections import namedtuple
import json
import pprint
import os.path

class Skill:
    def __init__(self, id, name, descr, xp, icon, unique, type):
        self.id = id
        self.name = name
        self.descr = descr
        self.xp = int(xp)
        self.icon = icon
        self.material_icon = f'!material-large:{icon}'
        self.unique = unique
        self.type = type

    def __str__(self):
        return self.name

    def __repr__(self):
        return pprint.pformat(vars(self))

class Achievement:
    def __init__(self, skill, metadata, user):
        self.skill = skill
        self.metadata = metadata
        self.user = user
    
    def xp(self):
        if 'xp' in self.metadata:
            return float(self.metadata['xp'])
        else:
            return self.skill.xp

skills_file = os.path.dirname(__file__) + '/all-skills.json'
with open(skills_file) as f:
    all_skills_json = json.load(f)
all_skills = {sk['id']: Skill(**sk) for sk in all_skills_json}