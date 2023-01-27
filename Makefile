# Makefile for TODO_PROJECT_NAME

# You can set these variables from the command line.
PYTHONSETUP	= python setup.py

SPHINXOPTS    = -n -v
SPHINXBUILD   = sphinx-build
SOURCEDIR     = doc/
BUILDDIR      = build

.PHONY: help clean install develop redevelop di dclean dinstall doc #test

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

clean:
	rm -rf $(BUILDDIR)/lib*
	rm -rf $(BUILDDIR)/dist*
	rm -rf .eggs/
	find TODO_PROJECT_NAME/ -name '*.pyc' -delete
	find TODO_PROJECT_NAME/ -name '*.so' -delete
	find TODO_PROJECT_NAME/ -name '*.c' -delete

install:
	$(PYTHONSETUP) install

develop:
	$(PYTHONSETUP) develop

redevelop:
	$(PYTHONSETUP) -q install --record _redevelop.txt
	xargs rm -rf < _redevelop.txt
	$(PYTHONSETUP) -q develop
	rm -f _redevelop.txt

doc:
	@$(SPHINXBUILD) -M html doc/source doc/build

dclean:
	rm -rf doc/build/
	find doc/ -name '*.pyc' -delete

build_test:
	pytest
test:
	pytest --cov-report term:skip-covered
