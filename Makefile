dev:
	pip install --upgrade pip pre-commit poetry
	poetry install
	pre-commit install
	poetry run pre-commit run --all-files

format:
	poetry run black day10 --target-version py310

lint: format
	poetry run flake8 day10/*.py

test:
	poetry run pytest --cov=day10 --cov-report=xml

coverage-html:
	poetry run pytest --cov=day10 --cov-report=html

pre-commit:
	pre-commit run --show-diff-on-failure

complexity-baseline:
	$(info Cyclomatic complexity index)
	poetry run xenon --max-absolute C --max-modules A --max-average A day10

mypy:
	poetry run mypy --pretty day10

pr:
	poetry run pre-commit run --all-files
