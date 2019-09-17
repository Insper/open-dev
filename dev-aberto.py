#!/usr/bin/env python3

import jinja2 as j2
import markdown
import os
import json
import pprint
import io
import re

import sys

from utils import load_key, create_key, write_string_to_file, load_encrypted, save_encrypted
from students import Student, all_students, Team, all_teams
from skills import Skill, all_skills


import click

from collections import namedtuple

PR = namedtuple('PR', ['project_name', 'url'])

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
    st = all_students[student_login]

    env = j2.Environment(loader=j2.FileSystemLoader('templates/'))

    feedback_template = env.get_template('report.md')
    sk_tutorial = [sk for sk in all_skills.values() if sk.type == 'Tutorial']

    print(st.achievements)

    for sk in sk_tutorial:

        for ach in st.achievements:
            if sk.id == ach.skill.id:
                sk.done = True


    with open(f'students/{student_login}-report.md', 'w') as f:
        f.write(feedback_template.render(sk_tutorial=sk_tutorial,
                                        tutorial_done=None, st=st))



    print(st.compute_grade())


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

def parse_url(url):
    m = re.match(r'https?://github.com/.*/([\w\-]+)/pull/(\d+)', url)
    if m:
        return PR(m.group(1), url)
    return PR('Outros', url)

def dict_add_to_list(d, el, url):
    if not el in d:
        d[el] = []
    d[el].append(url)

@dev_aberto_cli.command()
def build_site():
    env = j2.Environment(loader=j2.FileSystemLoader('templates/'))

    skill_template = env.get_template('skills.html')
    render_skill_type(skill_template, 'tutorial')
    render_skill_type(skill_template, 'code')
    render_skill_type(skill_template, 'community')
    render_skill_type(skill_template, 'docs')
    
    with open('docs/_snippets/alunos.md', 'w') as f:
        for student in sorted(all_students.keys()):
            student = all_students[student]
            f.write(f'* [{student.name.title()}](mailto:{student.login}@al.insper.edu.br)\n') 
        
    impacto_template = env.get_template('impact.html')
    
    prs = {}
    issues = {}
    for student in all_students.values():
        for ach in student.achievements:
            if ach.skill.id in [4, 5]:
                if isinstance(ach.metadata, dict):
                    url = ach.metadata['url']
                else:
                    url = ach.metadata
                data = parse_url(url)
                dict_add_to_list(prs, data.project_name, data.url)

            
            if ach.skill.id in [20, 21]:
                data = parse_url(ach.metadata)
                dict_add_to_list(issues, data.project_name, data.url)
    
    with open('docs/_snippets/prs-enviados.md', 'w') as f:
        f.write(impacto_template.render(data=prs))

    with open('docs/_snippets/issues-abertas.md', 'w') as f:
        f.write(impacto_template.render(data=issues))


if __name__ == '__main__':

    dev_aberto_cli()