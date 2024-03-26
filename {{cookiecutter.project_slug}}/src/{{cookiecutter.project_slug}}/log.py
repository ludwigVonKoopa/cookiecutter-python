import logging

logger = logging.getLogger(__name__)


class ColoredFormatter(logging.Formatter):
    """color logging messages"""

    CRITICAL = "\x1b[31;1m"  # bold red
    ERROR = "\x1b[38;5;196m"  # red
    WARNING = "\x1b[38;5;226m"  # yellow
    INFO = "\033[36m"  # blue
    DEBUG = "\033[34m"  # lightblue
    reset = "\x1b[0m"

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.DEBUG + self.fmt + self.reset,
            logging.INFO: self.INFO + self.fmt + self.reset,
            logging.WARNING: self.WARNING + self.fmt + self.reset,
            logging.ERROR: self.ERROR + self.fmt + self.reset,
            logging.CRITICAL: self.CRITICAL + self.fmt + self.reset,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def create_logger(name="{{ cookiecutter.project_name }}", level="INFO", filename=None):
    """build a logger with name and level wanted

    can be call again to change level of logger already initialized

    Parameters
    ----------
    name : str, optional
        name of the logger, by default "{{ cookiecutter.project_name }}"
    level : str or int, optional
        level of the logger, by default "WARNING"
    filename : str or None, optional
        if specified, log everything in a filename with debug level

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
    console.setLevel(level)
    _logger.addHandler(console)

    if filename is not None:
        filehandler = logging.FileHandler(
            filename,
        )
        filehandler.setFormatter(logging.Formatter(format_log))
        filehandler.setLevel(logging.DEBUG)
        _logger.addHandler(filehandler)

    _logger.setLevel(logging.DEBUG)
    _logger.debug("logger '%s' activated at level %s", name, level_name)
    return _logger
