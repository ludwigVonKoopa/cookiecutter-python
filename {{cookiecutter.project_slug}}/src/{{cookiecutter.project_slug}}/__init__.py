"""Top-level package for {{ cookiecutter.project_name }}."""

from importlib import metadata

from {{ cookiecutter.project_slug }} import log  # noqa: F401

__version__ = metadata.version(__package__)
__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'

del metadata
