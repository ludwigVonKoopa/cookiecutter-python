.PHONY: clean clean-build clean-pyc clean-test coverage dist doc help install lint lint/flake8

.DEFAULT_GOAL := help


define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr src/*.egg-info
	find . -name '*.egg-info' -delete
	find . -name '*.egg' -delete

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -delete
	find . -name '*.so' -delete
	find . -name '*.c' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete
	find . -name '__pycache__' -delete

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	ruff check
	ruff format
	pre-commit run --all-files


lint: lint/flake8 ## check style

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox


doc: ## generate Sphinx HTML documentation, including API docs
	sphinx-build -M html doc/source doc/build

dclean:
	rm -rf doc/build
	rm -rf doc/source/_autosummary
	{% if cookiecutter.create_matplotlib_gallery -%}
		rm -rf doc/source/gallery
	{%- endif %}
	find doc/ -name '*.pyc' -delete

{% if cookiecutter.create_matplotlib_gallery -%}
generate_ref:
	pytest --mpl-generate-path=tests/baseline -m new
{%- endif %}

install: clean ## install the package to the active Python's site-packages

	pip install .

develop:
	pip install -e .

profile:
	# python -m cProfile -o profiling2.pyprof <command>
