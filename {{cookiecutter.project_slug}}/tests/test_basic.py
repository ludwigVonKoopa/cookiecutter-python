import {{ cookiecutter.project_name }}


def test_imports():
    import {{ cookiecutter.project_name }}  # noqa: F401


def test_version():
    assert {{ cookiecutter.project_name }}.__version__ is not None
