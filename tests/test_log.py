import start_project


class Test_Log:
    def test_init(self):
        logger = start_project.log.create_logger()

        assert logger.name == "start_project"
        assert logger.level == 20

    def test_change_level(self):
        logger = start_project.log.create_logger()  # noqa: F841
