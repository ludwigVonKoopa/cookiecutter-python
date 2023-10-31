from importlib import metadata

from TODO_PROJECT_NAME import log  # noqa: F401

__version__ = metadata.version(__package__)

del metadata
