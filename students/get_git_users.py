import os 
import json

def filter_by_python_files(name):
  return name.find('.') < 0 and name.find('-achievements') < 0

files = os.listdir('./')



filtered_files = []
students = []
for file in files:
  if filter_by_python_files(file) and file != '__pycache__':
    with open(f'./{file}') as f:
      file_content = f.read()
      student_json = json.loads(file_content)
      git_user = student_json['ghuser']
      print(f'@{git_user}')
      students.append(f'@{git_user}')
    filtered_files.append(file)
