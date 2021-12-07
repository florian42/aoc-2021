dev:
	pip install --upgrade pip pre-commit poetry
	poetry install
	pre-commit install
	poetry run pre-commit run --all-files

format:
	poetry run black day7

lint: format
	poetry run flake8 day7/*.py

test:
	poetry run pytest --cov=day7 --cov-report=xml

coverage-html:
	poetry run pytest --cov=day7 --cov-report=html

pre-commit:
	pre-commit run --show-diff-on-failure

complexity-baseline:
	$(info Cyclomatic complexity index)
	poetry run xenon --max-absolute C --max-modules A --max-average A day7

mypy:
	poetry run mypy --pretty day7

pr:
	poetry run pre-commit run --all-files
