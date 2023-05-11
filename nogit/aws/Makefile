SHELL=/bin/bash
PATH := .venv/bin:$(PATH)


install:
	@[ ! -d .venv ] && python3 -m venv --copies .venv ||:;
	@( \
		source .venv/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements-dev.txt; \
	)