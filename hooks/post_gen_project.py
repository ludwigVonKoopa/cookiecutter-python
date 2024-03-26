#!/usr/bin/env python
import pathlib

if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        pathlib.Path("AUTHORS.rst").unlink()
        pathlib.Path("doc", "authors.rst").unlink()

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        pathlib.Path("LICENSE").unlink()
