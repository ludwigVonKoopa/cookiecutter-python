import {{ cookiecutter.project_name }}


class Test_Log:
    def test_init(self):
        logger = {{ cookiecutter.project_name }}.log.create_logger()

        assert logger.name == "{{ cookiecutter.project_name }}"
        assert logger.level == 20

    def test_change_level(self):
        logger = {{ cookiecutter.project_name }}.log.create_logger()  # noqa: F841
