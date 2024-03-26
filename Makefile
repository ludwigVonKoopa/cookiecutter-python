BAKE_OPTIONS=--no-input

help:
	@echo "bake 	Generate project using defaults"
	@echo "help 	Show this help"
	@echo "test 	Run the tests"
	@echo "replay 	Replay last cookiecutter run and watch for changes"
	@echo "watch 	Generate project using defaults and watch for changes"


bake:  # Generate project using defaults
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists
