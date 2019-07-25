
from collections import namedtuple
import pprint

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


Achievement = namedtuple('Achievement', ['skill_id', 'metadata'])