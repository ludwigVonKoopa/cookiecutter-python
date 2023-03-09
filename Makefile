# Makefile for TODO_PROJECT_NAME

.PHONY: help clean install develop redevelop di dclean dinstall doc check #test

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean		clean all files builded"
	@echo "  install	install TODO_PROJECT_NAME"
	@echo "  develop	install TODO_PROJECT_NAME in develop mode"
	@echo "  redevelop	fully install TODO_PROJECT_NAME in develop mode (can resolve problems)"
	@echo "  doc		install the documentation"
	@echo "  dclean		clean all documentation file builded"
	@echo "  dinstall	complete rebuild code then documentation"
	@echo "  test		start test exemples"
	@echo "  build_test	start test exemples"
	@echo "  check  	start test exemples"

clean:
	rm -rf build/
	rm -rf .eggs/
	find src/TODO_PROJECT_NAME/ -name '*.pyc' -delete
	find src/TODO_PROJECT_NAME/ -name '*.so' -delete
	find src/TODO_PROJECT_NAME/ -name '*.c' -delete

install:
	pip install .

develop:
	pip install -e .

redevelop:
	$(PYTHONSETUP) -q install --record _redevelop.txt
	xargs rm -rf < _redevelop.txt
	$(PYTHONSETUP) -q develop
	rm -f _redevelop.txt

doc:
	sphinx-build -M html doc/source doc/build

dclean:
	rm -rf doc/build/
	find doc/ -name '*.pyc' -delete

test:
	pytest

check:
	isort .
	flake8
	mypy --strict
