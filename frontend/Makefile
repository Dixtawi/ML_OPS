PYTHON_INTERPRETER = python3

all: requirements
	@echo "Bonjour! Ceci est une Makefile pour télécharger les dépendances"

requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

run:
	$(PYTHON_INTERPRETER) "instance/run.py"

