
from collections import namedtuple
import json
import pprint
import os.path

class Skill:
    def __init__(self, id, name, descr, xp, image_path, unique, type):
        self.id = id
        self.name = name
        self.descr = descr
        self.xp = int(xp)
        self.image_path = image_path
        self.unique = unique
        self.type = type

    def __repr__(self):
        return pprint.pformat(vars(self))


Achievement = namedtuple('Achievement', ['skill', 'metadata'])

skills_file = os.path.dirname(__file__) + '/all-skills.json'
with open(skills_file) as f:
    all_skills_json = json.load(f)
all_skills = {sk['id']: Skill(**sk) for sk in all_skills_json}