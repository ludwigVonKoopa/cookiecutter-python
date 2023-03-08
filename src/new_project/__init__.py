import pkg_resources

from TODO_PROJECT_NAME import log  # noqa: F401

__version__ = pkg_resources.get_distribution('TODO_PROJECT_NAME').version  # noqa: F401
del pkg_resources
