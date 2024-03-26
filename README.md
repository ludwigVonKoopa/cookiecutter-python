# Cookiecutter python

Cookiecutter template for a Python basic package.

## Features

* default development tools pre-configured
  * pre-commit, ruff, isort, version project from git tags
* `pytest` setup for testing with coverage
* small documentation setup with `sphinx`, pydata theme and api page
* command line interface pre-configured
* `logging` setup already done


.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter


## Quickstart

Install cookiecutter and generate a new python project:

```bash
  pip install cookiecutter
  cookiecutter https://github.com/ludwigVonKoopa/cookiecutter-python.git
```

Cookiecutter prompts you for information regarding your project. If not sure, just press enter and it will use default values:

```no-highlight
  [1/9] full_name (LudwigVonKoopa):
  [2/9] email (49512274+ludwigVonKoopa@users.noreply.github.com):
  [3/9] github_username (ludwigVonKoopa):
  [4/9] project_name (awesome-project):
  [5/9] project_slug (awesome_project):
  [6/9] project_short_description (Python Boilerplate contains all the boilerplate you need to create a Python package.):
  [7/9] conda_env_name (py_awesome_project):
  [8/9] create_author_file (y):
  [9/9] Select open_source_license
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    Choose from [1/2/3/4/5/6] (1):
```

There you go - you just created a minimal python project:

```no-highlight
awesome_project/
├── AUTHORS.rst
├── CHANGELOG.md
├── CODE_OF_CONDUCT.rst
├── CONTRIBUTING.rst
├── doc
│   ├── make.bat
│   ├── Makefile
│   └── source
│       ├── api.rst
│       ├── authors.rst
│       ├── changelog.rst
│       ├── conf.py
│       ├── contributing.rst
│       ├── index.rst
│       ├── installation.rst
│       ├── readme.rst
│       ├── _templates
│       │   ├── custom-class-template.rst
│       │   └── custom-module-template.rst
│       └── usage.rst
├── environment_dev.yml
├── environment.yml
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pyproject.toml
├── README.rst
├── requirements_dev.txt
├── src
│   └── awesome_project
│       ├── cli.py
│       ├── awesome_project.py
│       ├── __init__.py
│       └── log.py
└── tests
    ├── test_basic.py
    └── test_log.py
```

Then:

* get to your newly created project `cd mynewproject`
* create your conda environment `conda env create -f environment_dev.yml`
