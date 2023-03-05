import argparse
import logging

logger = logging.getLogger(__name__)


class ColoredFormatter(logging.Formatter):
    """Coloration syntaxique des message de logging
    """
    COLOR_LEVEL = dict(
        CRITICAL="\037[37;41m",
        ERROR="\033[31;47m",
        WARNING="\033[30;47m",
        INFO="\033[36m",
        DEBUG="\033[34m",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def format(self, record):
        color = self.COLOR_LEVEL[record.levelname]
        color_reset = '\033[0m'
        model = color + "%-7s" + color_reset
        record.msg = model % record.msg
        record.funcName = model % record.funcName
        record.name = model % record.name
        record.levelname = model % record.levelname
        return super(ColoredFormatter, self).format(record)


def create_logger(name="TODO_PROJECT_NAME", level="INFO"):
    """build a logger with name and level wanted

    can be call again to change level of logger already initialized

    Parameters
    ----------
    name : str, optional
        name of the logger, by default "TODO_PROJECT_NAME"
    level : str or int, optional
        level of the logger, by default "WARNING"

    Returns
    -------
    logging.Logger
        logger created
    """

    # set a format for console use
    format_log = "%(asctime)s - %(levelname)-10s %(name)s.%(funcName)s : %(message)s"

    _logger = logging.getLogger(name)
    level_name = logging.getLevelName(level) if isinstance(level, int) else level

    # si le logger existe déjà, on ne fait rien
    if len(_logger.handlers) > 0:
        if _logger.level != level:
            _logger.setLevel(level)
            _logger.info("changed logging level to %s", level_name)
        return _logger


    # set up logging to console
    console = logging.StreamHandler()
    console.setFormatter(ColoredFormatter(format_log))

    _logger.addHandler(console)
    _logger.setLevel(level)
    _logger.info("logger '%s' activated at level %s", name, level_name)
    return _logger
