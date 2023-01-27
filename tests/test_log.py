from TODO_PROJECT_NAME.log import create_logger


class Test_Log:
    def test_init(self):
        logger = create_logger()

        assert logger.name == "TODO_PROJECT_NAME"
        assert logger.level == 20

    def test_change_level(self):
        logger = create_logger()