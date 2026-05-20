#----- Comands -----
VENV = venv
PYTHON = $(VENV)/bin/python3
MYPY = $(VENV)/bin/mypy
FLAKE8 = $(VENV)/bin/flake8
PIP = $(VENV)/bin/pip
#----- Targets -----
.PHONY: help, install, lint, test, listS, run, debug, clean

help:
	@echo "***Wellcome to our project!***"
	@echo "Comands available:"
	@echo "  help    - show this help message"
	@echo "  run     - run the main program"
	@echo "  test    - run the tests"
	@echo "  lint    - analyze the code with flake8 and mypy"
	@echo "  lintS   - analyze the code with flake8 strict and mypy strict"
	@echo "  debug   - run the main program with the debugger"
	@echo "  clean   - remove temporary files and cache"
	@echo "  install  - install the dependencies from requirements.txt"

install: requirements.txt
	echo "Creating env"
	python3 -m venv venv 
	echo "Install requirements"
	$(PIP) install -r requirements.txt

lint:
	echo $(pwd)
	$(MYPY) . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
	$(FLAKE8) .

test:
	$(PY) -m pytest tests

lintS:
	$(MYPY) . --strict
	$(FLAKE8) . --strict

run: install
	echo "Executing program"
	$(PYTHON) a_maze_ing.py ee
debug:
	echo "Debub WIP"

clean:
	rm -rf __pycache__
	rm -rf venv