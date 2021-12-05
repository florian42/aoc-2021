dev:
	pip install --upgrade pip pre-commit poetry
	poetry install
	pre-commit install
	poetry run pre-commit run --all-files

format:
	poetry run black day5

lint: format
	poetry run flake8 day5/*.py

test:
	poetry run pytest --cov=day5 --cov-report=xml

coverage-html:
	poetry run pytest --cov=day5 --cov-report=html

pre-commit:
	pre-commit run --show-diff-on-failure

complexity-baseline:
	$(info Cyclomatic complexity index)
	poetry run xenon --max-absolute C --max-modules A --max-average A day5

mypy:
	poetry run mypy --pretty day5

pr:
	poetry run pre-commit run --all-files
