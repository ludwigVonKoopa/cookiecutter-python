import glob
import logging
import os
import shutil
import sys
import tempfile

import pytest
import sphinx.cmd.build

import start_project.appli

logger = logging.getLogger("start_project")
logger.setLevel("DEBUG")

OUTPUT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../output/test_creation")
)
os.makedirs(OUTPUT_PATH, exist_ok=True)


@pytest.fixture(scope="function")
def random_folder():
    path = tempfile.mkdtemp(prefix="test", dir=OUTPUT_PATH)
    print(path)
    yield path
    shutil.rmtree(path)


def rm_project_folders(project_name):
    # .../envs/../lib/python3.10/site-packages/
    site_package = os.path.dirname(os.path.dirname(pytest.__file__))

    folders = glob.glob(os.path.join(site_package, f"{project_name}*"))
    for folder in folders:
        shutil.rmtree(folder)


def test_if_it_runs(random_folder):

    start_project.appli.install_project(
        "test", random_folder, "Daphnès Nohansen", "superenv"
    )
    assert os.path.exists(os.path.join(random_folder, "test"))


def test_if_files_are_copied(random_folder):

    start_project.appli.install_project("oui", random_folder, "Pink Floyd", "superenv")
    list_files = sorted(
        os.listdir(
            os.path.join(
                random_folder,
                "oui",
            )
        )
    )
    print(list_files)
    assert list_files == [
        ".git",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".tmp_gitlab-ci.yml",
        "CHANGELOG.md",
        "Makefile",
        "README.md",
        "doc",
        "environment.yml",
        "environment_dev.yml",
        "pyproject.toml",
        "requirements.txt",
        "setup.cfg",
        "src",
        "tests",
        "todo.md",
    ]


def test_exception_if_folder_already_exist(random_folder):

    start_project.appli.install_project("non", random_folder, "Jean Michel", "superenv")
    with pytest.raises(FileExistsError):
        start_project.appli.install_project(
            "non", random_folder, "Yves Descendant", "superenv"
        )


def test_git_creation(random_folder):

    start_project.appli.install_project(
        "ptet", random_folder, "Yves cailloux", "superenv", init_git=True
    )
    assert os.path.exists(os.path.join(random_folder, "ptet", ".git"))


class Test_common_version:
    def test_compilation(self, random_folder):

        project_name = "my_super_project1"
        project_path = start_project.appli.install_project(
            project_name, random_folder, "Jean-Michel A-peu-pres", "superenv1"
        )
        os.system(f"pip install {project_path}")
        executable_folder = os.path.dirname(
            sys.executable
        )  # !which python   without "python"

        executable = os.path.join(executable_folder, f"{project_name}_example_script")
        assert os.path.exists(executable)
        os.system(executable)
        rm_project_folders(project_name)

    def test_doc(self, random_folder):

        project_name = "my_super_project1_doc"
        project_path = start_project.appli.install_project(
            project_name, random_folder, "Johnny Halliday", "superenv1"
        )
        os.system(f"pip install {project_path}")

        sphinx.cmd.build.main(
            [
                "-M",
                "html",
                os.path.join(project_path, "doc/source"),
                os.path.join(project_path, "doc/build"),
            ]
        )

        assert os.path.exists(os.path.join(project_path, "doc/build/html/index.html"))
        rm_project_folders(project_name)


class Test_matplotlib_version:
    def test_compilation(self, random_folder):
        project_name = "my_super_project2"
        project_path = start_project.appli.install_project(
            project_name, random_folder, "Gridania", "superenv2", matplotlib=True
        )
        os.system(f"pip install {project_path}")
        executable_folder = os.path.dirname(
            sys.executable
        )  # !which python   without "python"

        executable = os.path.join(executable_folder, f"{project_name}_example_script")
        assert os.path.exists(executable)
        os.system(executable)
        rm_project_folders(project_name)

    def test_doc(self, random_folder):
        project_name = "my_super_project2_doc"
        project_path = start_project.appli.install_project(
            project_name, random_folder, "Van Dome", "superenv2", matplotlib=True
        )
        os.system(f"pip install {project_path}")

        sphinx.cmd.build.main(
            [
                "-M",
                "html",
                os.path.join(project_path, "doc/source"),
                os.path.join(project_path, "doc/build"),
            ]
        )

        assert os.path.exists(os.path.join(project_path, "doc/build/html/index.html"))
        rm_project_folders(project_name)


# def test_building_doc(self, random_folder):
#     project_name = "my_super_project2"

#     project_path = start_project.appli.install_project(
#         project_name, random_folder, "Jean Michel", "superenv"
#     )
#     os.system(f"pip install {project_path}")

#     sphinx.cmd.build.main(
#         [
#             "-M",
#             "html",
#             os.path.join(project_path, "doc/source"),
#             os.path.join(project_path, "doc/build"),
#         ]
#     )
#     # print(os.path.join(project_path, "doc/source"))
#     assert os.path.exists(os.path.join(project_path, "doc/build/html/index.html"))
#     rm_project_folders(project_name)

#     # os.system(os.path.join(executable_folder, "my_script"))
