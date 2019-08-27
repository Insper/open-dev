#!/usr/bin/env python3

import jinja2 as j2
import markdown
import os
import json
import pprint
import io


import sys

from utils import load_key, create_key, write_string_to_file, load_encrypted, save_encrypted
from students import Student, all_students, Team, all_teams
from skills import Skill, all_skills


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
    
    print(all_students[student_login].compute_grade())


@dev_aberto_cli.command()
def list_users():
    for st in all_students.values():
        k = '*' if st.has_key else ''
        print(f'{st.name}{k}')

@dev_aberto_cli.command()
@click.argument('team_name')
def new_team(team_name):
    students = []
    while True:
        student_login = input('Login:')
        if student_login == '':
            break
        students.append(student_login)
    
    t = Team(team_name, students, [])

    with open(f'students/team-{team_name}', 'w') as f:
        f.write(t.toJSON())

@dev_aberto_cli.command()
def list_teams():
    for t in all_teams:
        print(t.name)

def render_skill_type(template, sk_type):
    skills_type = [sk for sk in all_skills.values() if sk.type == sk_type.title()]
    with open(f'docs/_snippets/skills-{sk_type}.md', 'w') as f:
        f.write(template.render(skills=skills_type))

@dev_aberto_cli.command()
def build_site():
    env = j2.Environment(loader=j2.FileSystemLoader('templates/'))

    skill_template = env.get_template('skills.html')
    render_skill_type(skill_template, 'tutorial')
    render_skill_type(skill_template, 'code')
    render_skill_type(skill_template, 'community')
    render_skill_type(skill_template, 'docs')
    
    # TODO: chamar gh-deploy





if __name__ == '__main__':

    dev_aberto_cli()