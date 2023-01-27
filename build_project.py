#!/usr/bin/env python

import os

def ask_question(question, lower=True):

    project_name_ok = False
    while not project_name_ok:
        ask = f"{question} ? (without caps)" if lower else f"{question} ?"

        print("#"*len(ask))
        print(ask)
        ANSWER = input()
        ANSWER = ANSWER.lower()

        print()
        print(f"{question} will be '{ANSWER}'. Is it ok ? [yes/no, y/n]")
        x = input()
        if x in ["yes", "y"]:
            project_name_ok = True

    return ANSWER

def start_cmd(cmd):
    print(cmd)
    os.system(cmd)

abspath = os.path.abspath('.')

PROJECT_NAME = ask_question("name of the project")
PROJECT_PATH = ask_question("absolute path to install project")
USER_NAME    = ask_question("name of the user", lower=False)
CONDA_ENV_NAME = ask_question("conda environment name", lower=False)


PROJECT_FULL_PATH = os.path.join(PROJECT_PATH, PROJECT_NAME)

if os.path.exists(PROJECT_FULL_PATH):
    print(f"there is already a project called '{PROJECT_NAME}' inside folder '{PROJECT_PATH}'. Please change project name, or project path, or delete already existing project then start again")
    exit()


# copy project in right folder
start_cmd(f"rsync -av  {abspath}/ {PROJECT_FULL_PATH} --exclude .git")
start_cmd(f"mv -v {os.path.join(PROJECT_FULL_PATH, 'new_project')} {os.path.join(PROJECT_FULL_PATH, PROJECT_NAME)}")

# search and replace TODO tags associated with project variables
start_cmd(f"find {PROJECT_FULL_PATH} -type f | xargs  sed -i 's/TODO\_env\_name/{CONDA_ENV_NAME}/'")
start_cmd(f"find {PROJECT_FULL_PATH} -type f | xargs  sed -i 's/TODO\_USER\_NAME/{USER_NAME}/'")
start_cmd(f"find {PROJECT_FULL_PATH} -type f | xargs  sed -i 's/TODO\_PROJECT\_NAME/{PROJECT_NAME}/'")

# change README from metaproject to actual project
start_cmd(f"rm -rfv {os.path.join(PROJECT_FULL_PATH, 'README.rst')}")
start_cmd(f"mv -v {os.path.join(PROJECT_FULL_PATH, 'README_after_build.rst')} {os.path.join(PROJECT_FULL_PATH, 'README.rst')}")

print()
print(f"project builded in '{PROJECT_FULL_PATH}' !")