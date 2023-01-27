#!/usr/bin/env python

from setuptools import setup, find_packages
import glob

with open("requirements.txt", "r") as fh:
    requirements = fh.read().split("\n")



setup(
    name="TODO_PROJECT_NAME",
    use_scm_version={
        'write_to': 'TODO_PROJECT_NAME/_version.py',
    },
    python_requires=">=3.9",
    description="TODO_DESCRIPTION",
    classifiers=[
        "Development Status :: 1 - Beta",
        "Topic :: ",
        "Programming Language :: Python",
    ],
    keywords="",

    packages=find_packages(),
    package_data={'': ["share/*",]},
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    scripts=[
        "scripts/new_project",
    ],
)
