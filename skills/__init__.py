
from collections import namedtuple
import json
import pprint
import os.path
import datetime
import types

def validate_type(obj, type_string):
    if 'List' in type_string:
        element_type = eval(type_string.split('[')[1][:-1])
        if not isinstance(obj, list):
            return False
        return all(isinstance(el, element_type) for el in obj) and len(obj) > 0
    
    return isinstance(obj, eval(type_string))

class Skill:
    def __init__(self, id, name, descr, xp, icon, unique, type, mandatory='-', metadata_requirements=[]):
        self.id = id
        self.name = name
        self.descr = descr
        self.xp = int(xp)
        self.icon = icon
        self.material_icon = f'!material-large:{icon}'
        self.unique = unique
        self.type = type
        self.mandatory = mandatory

        self.metadata_requirements = []
        for mt in metadata_requirements:
            field_name, field_type = mt.split('|')
            self.metadata_requirements.append((field_name, field_type))        

    def __str__(self):
        return self.name

    def __repr__(self):
        return pprint.pformat(vars(self))

class Achievement:
    def __init__(self, skill, metadata, user, date=datetime.date.today()):
        self.skill = skill
        self.metadata = metadata
        self.user = user
        self.date = date
    
    def __str__(self):
        return f'Achievement: skill_id: {self.skill.id}, date: {self.date}'


    def validate_metadata(self):
        for mt in self.skill.metadata_requirements:
            field_name, field_type = mt
            if not field_name in self.metadata:
                raise ValueError(f'Campo {field_name} não existe!')
            
            if not validate_type(self.metadata[field_name], field_type):
                raise ValueError(f'Campo {field_name} não é do tipo {field_type}')


    def xp(self):
        if not self.validate_metadata():
            return 0
        if 'xp' in self.metadata:
            return float(self.metadata['xp'])
        else:
            return self.skill.xp

skills_file = os.path.dirname(__file__) + '/all-skills.json'
with open(skills_file) as f:
    all_skills_json = json.load(f)
all_skills = {sk['id']: Skill(**sk) for sk in all_skills_json}