#!/usr/bin/env python
import pathlib
import shutil

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        pathlib.Path("LICENSE").unlink()

    if not {{cookiecutter.create_matplotlib_gallery}}:
        shutil.rmtree("examples")
        pathlib.Path("tests", "test_figure.py").unlink()
