# start_project

`start_project` is a tool to help you start a new project.

It can create for you a fully functionnal project, already configured, with examples that you can modify.
You give a project name and a path, and the tool will create:

* all folders and files for your project :
    * configuration files with correct options and names for your project,
    * setuptools, setup.cfg, .gitignore, pyproject.toml,
* default development tool preconfigured:
    * black, isort, flake8 or pre-commit already configured
    * a default but working pytests tests already implemented with **coverage** and html/terminal output
    * git tag automatically in the project version
* small but running documentation:
    * sphinx and sphinx extension already configured
* default script available when installing your library
* default and nice logging system, easily modifiable


# commands

To install the project, use

```bash
    pip install .
```

Then, use

```bash
    start-project
```

and use corrects argument to create your project.
