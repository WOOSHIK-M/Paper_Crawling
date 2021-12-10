.DEFAULT_GOAL := help

format:
	brunette . --config=setup.cfg
	isort .

lint:
	PYTHONPATH=src pytest src --pylint --flake8 --mypy

setup-dev:
	pip install -r "requirements-dev.txt"
	pre-commit install

tree:
	tree -I "*data|.pkl|*.png|*.txt|$(shell cat .gitignore | tr -s '\n' '|' )"
help:
	@echo "Usage: make [target]"
	@echo
	@echo "Available targets:"
	@echo "  format:"
	@echo "    Format the code"
	@echo "  lint:"
	@echo "    Lint the code with caching"
	@echo "  setup:"
	@echo "    Install the dependencies"
	@echo "  setup-dev:"
	@echo "    Install the dependencies for development"
	@echo "  tree:"
	@echo "    Show the directory tree"
	@echo
	@echo "  help:"
	@echo "    Show this help message"