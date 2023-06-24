# Installation
install:
	pip install -r requirements.txt
#run server
run:
	uvicorn main:app --reload --log-level info 

# Dev tools
black-check:
	black --config pyproject.toml --check --diff .

black-fix:
	black --config pyproject.toml .

ruff-check:
	ruff check .

ruff-fix:
	ruff check . --fix

check: black-check ruff-check

format: black-fix ruff-fix