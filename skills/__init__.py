
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
        return all(isinstance(el, element_type) for el in obj)
    if type_string == 'date':
        try:
            d = datetime.datetime.strptime(obj, '%Y-%m-%d')
        except ValueError:
            return False
        return True

    return isinstance(obj, eval(type_string))


class Skill:
    def __init__(self, id, name, descr, xp, icon, unique, type, multiplier=1,
                 mandatory='-', metadata_requirements=[], 
                 date_limit='2021-12-31', icon_version=4):
        self.id = id
        self.name = name
        self.descr = descr
        self.xp = int(xp)
        self.icon = icon
        self.icon_version = icon_version
        self.material_icon = f':material-{icon}:' + '{: .skill-icon }'
        self.unique = unique
        self.type = type
        self.multiplier = multiplier
        self.mandatory = mandatory
        self.date_limit = datetime.datetime.strptime(date_limit, '%Y-%m-%d')

        self.metadata_requirements = [('date', 'date')]
        for mt in metadata_requirements:
            field_name, field_type = mt.split('|')
            self.metadata_requirements.append((field_name, field_type))        

    def __str__(self):
        return self.name

    def __repr__(self):
        return pprint.pformat(vars(self))

class Achievement:
    def __init__(self, skill, metadata, user):
        self.skill = skill
        self.date = datetime.datetime.strptime(metadata['date'], '%Y-%m-%d')
        self.metadata = metadata
        self.user = user
    
    def __str__(self):
        return f'Achievement: skill_id: {self.skill.id}'


    def validate_metadata(self):
        for mt in self.skill.metadata_requirements:
            field_name, field_type = mt
            if not field_name in self.metadata:
                raise ValueError(f'Campo {field_name} não existe!')
            
            if not validate_type(self.metadata[field_name], field_type):
                raise ValueError(f'Campo {field_name} não é do tipo {field_type}')

    def xp(self):
        try:
            self.validate_metadata()
            if self.date > self.skill.date_limit:
                return 0
            if 'xp' in self.metadata:
                return float(self.metadata['xp'])
            else:
                return self.skill.xp
        except ValueError:
            return 0

skills_file = os.path.dirname(__file__) + '/all-skills.json'
with open(skills_file) as f:
    all_skills_json = json.load(f)
all_skills = {sk['id']: Skill(**sk) for sk in all_skills_json}