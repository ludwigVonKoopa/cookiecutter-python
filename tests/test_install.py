import os
import shutil
import tempfile

import pytest

import start_project.appli

OUTPUT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../output/test_creation")
)
os.makedirs(OUTPUT_PATH, exist_ok=True)


@pytest.fixture(scope="function")
def random_folder():
    path = tempfile.mkdtemp(prefix="test", dir=OUTPUT_PATH)
    yield path
    shutil.rmtree(path)


class Test_install_project:

    def test_if_it_runs(self, random_folder):

        start_project.appli.install_project(
            "test", random_folder, "Jean Michel", "superenv"
        )
        assert os.path.exists(os.path.join(random_folder, "test"))

    def test_if_files_are_copied(self, random_folder):

        start_project.appli.install_project(
            "oui", random_folder, "Jean Michel", "superenv"
        )
        list_files = sorted(
            os.listdir(
                os.path.join(
                    random_folder,
                    "oui",
                )
            )
        )
        assert list_files == [
            ".gitignore",
            ".pre-commit-config.yaml",
            ".tmp_gitlab-ci.yml",
            ".vscode",
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

    def test_exception_if_folder_already_exist(self, random_folder):

        start_project.appli.install_project(
            "non", random_folder, "Jean Michel", "superenv"
        )
        with pytest.raises(FileExistsError):
            start_project.appli.install_project(
                "non", random_folder, "Jean Michel", "superenv"
            )

    def test_git_creation(self, random_folder):

        start_project.appli.install_project(
            "ptet", random_folder, "Yves cailloux", "superenv", init_git=True
        )
        assert os.path.exists(os.path.join(random_folder, "ptet", ".git"))

    def test_usage(self):
        args = start_project.appli.usage()

    # def test_ask_question(self):
    #     start_project.appli.input = lambda: "moui"
    #     args = start_project.appli.ask_question("")
    #     start_project.appli.input = input
