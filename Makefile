VENV = venv
PYTHON = $(venv)/bin/python3
MYPY = $(venv)/bin/mypy
FLAKE8 = $(venv)/bin/flake8
PIP = $(venv)/bin/pip


setup: requirements.txt
	echo "Creating env"
	python3 -m venv venv 
	echo "Install requirements"
	$(PIP) install -r requirements.txt

lint:
	$(MYPY) . --strict
	$(FLAKE8) .


run: setup
	echo "Executing program"
	$(PYTHON) a_maze_ing.py ee

clean:
	rm -rf __pycache__
	rm -rf venv