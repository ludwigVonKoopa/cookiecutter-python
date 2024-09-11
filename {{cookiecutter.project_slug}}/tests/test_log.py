import {{ cookiecutter.project_slug }}
import logging

class Test_Log:
    def test_init(self):
        logger = {{ cookiecutter.project_slug }}.log.create_logger()

        assert logger.name == "{{ cookiecutter.project_slug }}"
        assert logger.level == logging.DEBUG
        assert logger.handlers[0].level == logging.DEBUG

    def test_other_level(self):
        logger = {{ cookiecutter.project_slug }}.log.create_logger(level="INFO")

        assert logger.name == "{{ cookiecutter.project_slug }}"
        assert logger.level == logging.DEBUG
        assert logger.handlers[0].level == logging.INFO

    def test_change_level(self):
        logger = {{ cookiecutter.project_slug }}.log.create_logger()  # noqa: F841

        assert logger.level == logging.DEBUG
        assert logger.handlers[0].level == logging.DEBUG

        logger = {{ cookiecutter.project_slug }}.log.create_logger(level="WARNING")  # noqa: F841

        assert logger.level == logging.DEBUG
        assert logger.handlers[0].level == logging.WARNING
