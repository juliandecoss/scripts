SHELL=/bin/bash
PATH := .venv/bin:$(PATH)
export TEST?=./tests
export LAMBDA?=platform-authentication
export ENV?=test

install:
	@( \
		if [ ! -d .venv ]; then python3 -m venv --copies .venv; fi; \
		source .venv/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements.txt; \
	)