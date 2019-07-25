#/usr/bin/env python3

import jinja2 as j2
import markdown
import os
import json
import pprint
import io


import sys

from utils import *
from students import Student
from skills import Skill


import click


@click.group()
def dev_aberto_cli():
    pass

@dev_aberto_cli.command()
def new_user():
    student_login = ''

    while student_login == '':
        student_login = input('login insper: ').strip()

    student_key = create_key(f'students/{student_login}.key')
    student_name = input('nome completo: ')
    student_avatar = input('imagem de avatar: ')
    s = Student(student_login, student_name, student_avatar, [])
    write_string_to_file(f'students/{student_login}', s.toJSON())
    
    save_encrypted(f'students/{student_login}-achievements', student_key, '[]')


@dev_aberto_cli.command()
@click.argument('student_login')
def edit_achievements(student_login):
    key = load_key(f'students/{student_login}.key')
    json_achievements = load_encrypted(f'students/{student_login}-achievements', key)

    with open(f'students/{student_login}.temp', 'w') as f:
        f.write(json_achievements)
    
    editor = os.getenv('EDITOR', default='vi')

    os.system(f'{editor} students/{student_login}.temp')

    with open(f'students/{student_login}.temp') as f:
        json_achievements = f.read()
    
    save_encrypted(f'students/{student_login}-achievements', key, json_achievements)

    os.remove(f'students/{student_login}.temp')


@dev_aberto_cli.command()
@click.argument('student_login')
def compute_grade(student_login):
    s = Student.load(student_login)
    print(s.compute_grade())


@dev_aberto_cli.command()
def build_website():
    skills = load_all_data()
    env = j2.Environment(loader=j2.FileSystemLoader('templates/'))
    skills_templ = env.get_template('skills.html')
    with open('docs/skills.html', 'w') as f:
        f.write(skills_templ.render(skills=skills))

    index_templ = env.get_template('index.html')
    with open('docs/index.html', 'w') as f:
        f.write(index_templ.render(show_header=True))

if __name__ == '__main__':

    dev_aberto_cli()