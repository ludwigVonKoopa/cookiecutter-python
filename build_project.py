#!/usr/bin/env python

import argparse
import os


def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-path", help="absolute path to install project (without the name)", default=None)
    parser.add_argument("--project-name", help="name of the project (without the path)", default=None)
    parser.add_argument("--user-name", help="name of the user", default=None)
    parser.add_argument("--conda-env-name", help="conda environment name", default=None)
    return parser.parse_args()


def ask_question(question, lower=True):

    project_name_ok = False
    while not project_name_ok:
        ask = f"{question} ? (without caps)" if lower else f"{question} ?"

        print("#" * len(ask))
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

args = usage()
if args.project_path is None:
    PROJECT_PATH = ask_question("Q1/4 : absolute path to install project (without the name)")
else:
    PROJECT_PATH = args.project_path

if args.project_name is None:
    PROJECT_NAME = ask_question("Q2/4 : name of the project (without the path)")
else:
    PROJECT_NAME = args.project_name

if args.user_name is None:
    USER_NAME = ask_question("Q3/4 : name of the user")
else:
    USER_NAME = args.user_name

if args.conda_env_name is None:
    CONDA_ENV_NAME = ask_question("Q4/4 : conda environment name")
else:
    CONDA_ENV_NAME = args.conda_env_name


PROJECT_FULL_PATH = os.path.join(PROJECT_PATH, PROJECT_NAME)

if os.path.exists(PROJECT_FULL_PATH):
    print(f"there is already a project called '{PROJECT_NAME}' inside folder '{PROJECT_PATH}'. ")
    print("Please change project name, or project path, or delete already existing project then start again")
    exit()

fichiers = [
    "doc", "scripts", "src", "tests",
    ".coveragerc", ".gitignore", "CHANGELOG.md", "Makefile",
    "environment.yml", "environment_dev.yml", "pyproject.toml", "setup.cfg", "todo.md"
]


# copy project in right folder
for f in fichiers:
    if os.path.isdir(f"{abspath}/{f}"):
        cmd = f"mkdir -p {PROJECT_FULL_PATH}/{f}"
        start_cmd(cmd)
    cmd = f"cp -Rv {abspath}/{f} {PROJECT_FULL_PATH}/"
    start_cmd(cmd)
    print()

cmd = f"cp -Rv {abspath}/README_after_build.md {PROJECT_FULL_PATH}/README.md"
start_cmd(cmd)
start_cmd(f"mv -v {os.path.join(PROJECT_FULL_PATH, 'src/new_project')} {os.path.join(PROJECT_FULL_PATH, f'src/{PROJECT_NAME}')}")


# search and replace TODO tags associated with project variables
start_cmd(f"find {PROJECT_FULL_PATH} -type f | xargs  sed -i 's/TODO\_env\_name/{CONDA_ENV_NAME}/'")
start_cmd(f"find {PROJECT_FULL_PATH} -type f | xargs  sed -i 's/TODO\_USER\_NAME/{USER_NAME}/'")
start_cmd(f"find {PROJECT_FULL_PATH} -type f | xargs  sed -i 's/TODO\_PROJECT\_NAME/{PROJECT_NAME}/'")

print()
print(f"project builded in '{PROJECT_FULL_PATH}' !")
