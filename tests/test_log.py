import TODO_PROJECT_NAME


class Test_Log:
    def test_init(self):
        logger = TODO_PROJECT_NAME.log.create_logger()

        assert logger.name == "TODO_PROJECT_NAME"
        assert logger.level == 20

    def test_change_level(self):
        logger = TODO_PROJECT_NAME.log.create_logger()  # noqa: F841
