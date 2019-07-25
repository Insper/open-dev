from cryptography.fernet import Fernet
import sys
import json
from skills import Skill

def create_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'w') as f:
        f.write(key.decode('ascii'))
    return key

def load_key(key_file):
    try:
        with open(key_file) as f:
            key = f.read()
    except IOError:
        return None
        
    return key

def save_encrypted(filename, key, content):
    cypher = Fernet(key)
    with open(filename, 'w') as f:
        f.write(cypher.encrypt(content.encode('utf-8')).decode('utf-8'))
    

def load_encrypted(filename, key):
    cypher = Fernet(key)
    with open(filename) as f:
        encrypted = f.read()
        return cypher.decrypt(encrypted.encode('utf-8')).decode('utf-8')

def write_string_to_file(filename, string):
    with open(filename, 'w') as f:
        f.write(string)

def load_from_file(filename):
    with open(filename) as f:
        return f.read()



def load_from_json(json_path, class_obj):
    objs = []

    with open(json_path) as f:
        objs_json = json.load(f)
    
    for ob in objs_json:
        objs.append(class_obj(**ob))
    
    return objs






def load_all_data():
    skills = load_from_json('skills/all-skills.json', Skill)

    return skills
