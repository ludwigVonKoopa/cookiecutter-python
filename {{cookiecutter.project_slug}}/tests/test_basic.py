import {{ cookiecutter.project_slug }}


def test_imports():
    import {{ cookiecutter.project_slug }}  # noqa: F401


def test_version():
    assert {{ cookiecutter.project_slug }}.__version__ is not None
