import argparse
import logging
import os
import shutil

import start_project.log  # noqa: F401

logger = logging.getLogger(__name__)


def usage():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--verbose",
        action="store",
        help="verbose",
        choices=["ERROR", "WARNING", "INFO", "DEBUG"],
        default="INFO",
    )

    parser.add_argument(
        "project_name", help="name of the project (without the path)", default=None
    )
    parser.add_argument(
        "--project-path",
        help=(
            "absolute path to install project (without the name). If not precised, "
            "create the project where the command is started"
        ),
        default=".",
    )
    parser.add_argument(
        "--user-name", required=True, help="name of the user", default=None
    )
    parser.add_argument(
        "--conda-env-name",
        help="conda environment name. By default : {{project-name}}_env",
        default=None,
    )
    parser.add_argument(
        "--init-git",
        help="initialise the git repositery with first commit",
        action="store_true",
    )
    parser.add_argument(
        "--matplotlib",
        help="Create a project which contain a matplotlib gallery",
        action="store_true",
    )
    return parser.parse_args()


def ask_question(question, lower=True):

    name_ok = False
    while not name_ok:
        ask = f"{question} ? (without caps)" if lower else f"{question} ?"

        print("#" * len(ask))
        print(ask)
        ANSWER = input()
        ANSWER = ANSWER.lower()

        print()
        print(f"{question} will be '{ANSWER}'. Is it ok ? [yes/no, y/n]")
        x = input()
        if x in ["yes", "y"]:
            name_ok = True

    return ANSWER


def copy_and_eval(src, dest, PROJECT_NAME, USER_NAME, CONDA_ENV_NAME):

    with open(src) as f_in:
        code = f_in.read()

    code = code.replace("TODO_env_name", CONDA_ENV_NAME)
    code = code.replace("TODO_USER_NAME", USER_NAME)
    code = code.replace("TODO_PROJECT_NAME", PROJECT_NAME)

    logger.debug(f"creating file {dest}")
    with open(dest, "w") as f_out:
        f_out.write(code)


def install_project(
    PROJECT_NAME,
    PROJECT_PATH,
    USER_NAME,
    CONDA_ENV_NAME,
    init_git=True,
    matplotlib=False,
):

    logger.info(f"Project name   : {PROJECT_NAME}")
    logger.info(f"Project path   : {PROJECT_PATH}")
    logger.info(f"Creator name   : {USER_NAME}")
    logger.info(f"conda env name : {CONDA_ENV_NAME}")

    project_fullname = os.path.join(PROJECT_PATH, PROJECT_NAME)
    if os.path.exists(project_fullname):
        msg = f"There is already a project called '{PROJECT_NAME}' inside folder '{PROJECT_PATH}'."
        logger.error(msg)
        logger.error(
            "Please change project name, project path, or delete already existing project then start again"
        )
        raise FileExistsError(msg)

    os.makedirs(project_fullname)
    source_folder = os.path.join(os.path.dirname(__file__), "assets/common/")

    for path, directories, files in os.walk(source_folder):
        if "__pycache__" in path:
            continue

        output_path = os.path.join(project_fullname, path.replace(source_folder, ""))

        os.makedirs(output_path, exist_ok=True)
        for fichier in files:
            output_file = os.path.join(output_path, fichier)
            source_file = os.path.join(path, fichier)

            copy_and_eval(
                source_file, output_file, PROJECT_NAME, USER_NAME, CONDA_ENV_NAME
            )

    if matplotlib:
        source_folder = os.path.join(os.path.dirname(__file__), "assets/matplotlib/")
        for path, directories, files in os.walk(source_folder):

            if "__pycache__" in path:
                continue

            output_path = os.path.join(
                project_fullname, path.replace(source_folder, "")
            )

            os.makedirs(output_path, exist_ok=True)
            for fichier in files:
                output_file = os.path.join(output_path, fichier)
                source_file = os.path.join(path, fichier)

                copy_and_eval(
                    source_file, output_file, PROJECT_NAME, USER_NAME, CONDA_ENV_NAME
                )

    # raise Exception()

    if init_git:
        os.system(f"cd {project_fullname}; git init")
        os.system(f"cd {project_fullname}; ls; git add * .gitignore")
        os.system(f"cd {project_fullname}; git status")
        os.system(
            f"cd {project_fullname}; git commit -m \"project created with 'start_project'\""
        )

    shutil.move(
        os.path.join(project_fullname, "src", "TODO_PROJECT_NAME"),
        os.path.join(project_fullname, "src", PROJECT_NAME),
    )
    logger.info(f"Project '{PROJECT_NAME}' created !")
    logger.info(
        "Please check the 'readme.md' in your project to fill the last missing data"
    )
    return project_fullname


def cli():
    args = usage()
    print(args)
    start_project.log.create_logger(level=args.verbose)

    PROJECT_NAME = args.project_name
    PROJECT_PATH = os.path.abspath(args.project_path)
    USER_NAME = args.user_name
    CONDA_ENV_NAME = args.conda_env_name
    if CONDA_ENV_NAME is None:
        CONDA_ENV_NAME = f"{PROJECT_NAME}_env"

    install_project(
        PROJECT_NAME, PROJECT_PATH, USER_NAME, CONDA_ENV_NAME, init_git=args.init_git
    )
