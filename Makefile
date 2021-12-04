dev:
	pip install --upgrade pip pre-commit poetry
	poetry install
	pre-commit install
	poetry run pre-commit run --all-files

format:
	poetry run black day4

lint: format
	poetry run flake8 day4/*.py

test:
	poetry run pytest --cov=day4 --cov-report=xml

coverage-html:
	poetry run pytest --cov=day4 --cov-report=html

pre-commit:
	pre-commit run --show-diff-on-failure

release-docs:
	@echo "Rebuilding docs"
	rm -rf site api
	@echo "Updating website docs"
	poetry run mike deploy --push --update-aliases ${VERSION} ${ALIAS}
	@echo "Building API docs"
	@$(MAKE) build-docs-api

complexity-baseline:
	$(info Cyclomatic complexity index)
	poetry run xenon --max-absolute C --max-modules A --max-average A day4

mypy:
	poetry run mypy --pretty day4

pr:
	poetry run pre-commit run --all-files
