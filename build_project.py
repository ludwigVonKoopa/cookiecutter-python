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

PROJECT_NAME = ask_question("name of the project")
USER_NAME    = ask_question("name of the user", lower=False)
CONDA_ENV_NAME = ask_question("conda environment name", lower=False)

def start_cmd(cmd):
    print(cmd)
    os.system(cmd)

start_cmd(f"find . -type f | xargs  sed -i 's/TODO\_env\_name/{CONDA_ENV_NAME}/'")

start_cmd(f"find . -type f | xargs  sed -i 's/TODO\_USER\_NAME/{USER_NAME}/'")

start_cmd(f"find . -type f | xargs  sed -i 's/TODO\_PROJECT\_NAME/{PROJECT_NAME}/'")
start_cmd(f"mv -v new_project {PROJECT_NAME}")

start_cmd(f"rm -rfv README.rst")
start_cmd(f"mv -v README_after_build.rst README.rst")
