VENV = venv
PYTHON = $(VENV)/bin/python3
MYPY = $(VENV)/bin/mypy
FLAKE8 = $(VENV)/bin/flake8
PIP = $(VENV)/bin/pip


install: requirements.txt
	echo "Creating env"
	python3 -m venv venv 
	echo "Install requirements"
	$(PIP) install -r requirements.txt

lint:
	echo $(pwd)
	$(MYPY) . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
	$(FLAKE8) .


run: setup
	echo "Executing program"
	$(PYTHON) a_maze_ing.py ee
debug:
	echo "Debub WIP"

clean:
	rm -rf __pycache__
	rm -rf venv