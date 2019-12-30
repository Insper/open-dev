#!/usr/bin/env python3

import jinja2 as j2
import markdown
import os
import json
import pprint
import io
import re
import copy
import markdown
import tabulate

import sys
import time

from utils import load_key, create_key, write_string_to_file, load_encrypted, save_encrypted
from students import Student, all_students, project_points
from skills import Skill, all_skills


import click

from collections import namedtuple

PR = namedtuple('PR', ['project_name', 'url', 'status'])

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
    
    if 'win32' in sys.platform:
        editor = os.getenv('EDITOR', default='notepad.exe')
    else:
        editor = os.getenv('EDITOR', default='vi')
    
    valid_json = False
    while not valid_json:
        os.system(f'{editor} students/{student_login}.temp')
        with open(f'students/{student_login}.temp') as f:
            json_achievements = f.read()
        try:
            _ = json.loads(json_achievements)
            valid_json = True
        except json.JSONDecodeError:
            print("Arquivo mal formatado.")
            time.sleep(2)
    save_encrypted(f'students/{student_login}-achievements', key, json_achievements)

    os.remove(f'students/{student_login}.temp')

def load_skill_and_check_done(skill_name, st):
    skill_list = [copy.deepcopy(sk) for sk in all_skills.values() if sk.type == skill_name]
    for sk in skill_list:
        sk.done = False
        if sk.id in [3, 11, 12]:
            sk.done = True # nao eh obrigatoria
        for ach in st.achievements:
            if sk.id == ach.skill.id:
                sk.done = True
    return skill_list


@dev_aberto_cli.command()
@click.argument('student_login')
def compute_grade(student_login):
    print(f'{student_login}:')
    st = all_students[student_login]

    env = j2.Environment(loader=j2.FileSystemLoader('templates/'))

    feedback_template = env.get_template('report.html')
    
    sk_tutorial = load_skill_and_check_done('Tutorial', st)
    sk_docs = load_skill_and_check_done('Docs', st)
    sk_code = load_skill_and_check_done('Code', st)
    sk_comm = load_skill_and_check_done('Community', st)    

    xp = st.compute_grade()

    print('------------')
    conceito = 'I'
    comentario_conceito = 'Atividades de sala de aula não concluídas\n'
    if all([sk.done for sk in sk_tutorial]):
        conceito = 'D'
        print('Conceito D alcançado.')
        if (any([sk.done for sk in sk_docs]) and 
            any([sk.done for sk in sk_code]) and 
            any([sk.done for sk in sk_comm])) and xp >= 60:
            conceito = 'C'
        else:
            print('------------')
            comentario_conceito = ''
            if any([sk.done for sk in sk_docs]) == False:
                print('Conceito C: Skill de Documentação faltando.')
                comentario_conceito = '\tSkill de Documentação faltando.\n'
            if any([sk.done for sk in sk_code]) == False:
                print('Conceito C: Skill de Código faltando.')
                comentario_conceito += '\tSkill de Código faltando.\n'
            if any([sk.done for sk in sk_comm]) == False:
                print('Conceito C: Skill de Comunidade faltando.')
                comentario_conceito += '\tSkill de Comunidade faltando.\n'
    else:
        for sk in sk_tutorial:
            if sk.done == False:
                print('Skill de tutorial faltante:', sk.name)
                comentario_conceito += f'\t{sk.name}\n'
    
    html = feedback_template.render(sk_tutorial=sk_tutorial,
                                      sk_code=sk_code,
                                      sk_docs=sk_docs,
                                      sk_comm=sk_comm,
                                      xp_total=xp, st=st, conceito=conceito,
                                      comentario_conceito=comentario_conceito
                                    )
    with open(f'students/{student_login}-report.html', 'w') as f:
        f.write(html)

    print('------------')
    print('Conceito final:', conceito)
    print(xp)
    print('Nota de grupo:', project_points[student_login])

@dev_aberto_cli.command()
@click.pass_context
def report_cards(ctx):
    print(ctx, all_students.keys())
    for st_login in all_students.keys():
        print('st_login', st_login)        
        ctx.invoke(compute_grade, student_login=st_login)

    # TODO: envia e-mail

@dev_aberto_cli.command()
def list_users():
    for st in all_students.values():
        k = '*' if st.has_key else ''
        print(f'{st.name}{k}')

def render_skill_type(sk_type):
    table = [(sk.id, sk.material_icon, sk.name, sk.descr, sk.xp)
                for sk in all_skills.values() if sk.type == sk_type.title()]
    with open(f'docs/_snippets/skills-{sk_type}.md', 'w') as f:
        f.write(tabulate.tabulate(table, headers=('id', '', 'Nome', 'Descrição', 'XP'), tablefmt='pipe'))

def parse_url(url):
    m = re.match('https?://github.com/(.*)/([\w\-]+)/(pull|issues)/(\d+)', url)
    if m:
        if m.group(3) == "pull":
            pulls_issues = "pulls"
        else:
            pulls_issues = "issues"
        status = "https://img.shields.io/github/"+ pulls_issues +"/detail/state/" + m.group(1)+"/"+m.group(2)+"/"+ m.group(4)+ "?label=%20"
        return PR(m.group(2), url, status)
    return PR('Outros', url, '')

def dict_add_to_list(d, el, url):
    if not el in d:
        d[el] = []
    d[el].append(url)

def dict_add_to_dict(d, el, sub, url):
    if not el in d:
        d[el] = {}
    if not sub in d[el]:
        d[el][sub] = []
    d[el][sub].append(url)

@dev_aberto_cli.command()
def build_site():
    env = j2.Environment(loader=j2.FileSystemLoader('templates/'))

    render_skill_type('tutorial')
    render_skill_type('code')
    render_skill_type('community')
    render_skill_type('docs')
    
    students = []
    for st_login in sorted(all_students.keys()):
        st = all_students[st_login]
        students.append([
            f'![{st.name}]({st.avatar}){{: style="max-width:64px; valign="center"}}',
            st.name.title(), 
            f'[![](css/github.png)](http://github.com/{st.ghuser})'
        ])
    with open('docs/_snippets/alunos.md', 'w') as f:
        f.write(tabulate.tabulate(students, headers=('', '', ''), tablefmt='pipe'))
        
    impacto_template = env.get_template('impact.html')
    info = {}    
    for student in all_students.values():
        for ach in student.achievements:
            if ach.skill.id in [4, 5] and ach.user == student:
                if isinstance(ach.metadata, dict):
                    url = ach.metadata['url']
                else:
                    url = ach.metadata
                print(url)

                data = parse_url(url)
                dict_add_to_dict(info, data.project_name, 'Pull Requests', data)

            
            if ach.skill.id in [20, 21] and ach.user == student:
                if isinstance(ach.metadata, dict):
                    url = ach.metadata['url']
                else:
                    url = ach.metadata
                data = parse_url(url)
                dict_add_to_dict(info, data.project_name, 'Issues', data)

    with open('docs/_snippets/impacto.md', 'w') as f:
        f.write(impacto_template.render(data=info))

if __name__ == '__main__':

    dev_aberto_cli()
