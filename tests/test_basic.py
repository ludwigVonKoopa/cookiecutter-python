import start_project


def test_imports():
    import start_project  # noqa: F401


def test_version():
    assert start_project.__version__ is not None
