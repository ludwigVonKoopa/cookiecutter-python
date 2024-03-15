from importlib import metadata

from start_project import log  # noqa: F401

__version__ = metadata.version(__package__)

del metadata
