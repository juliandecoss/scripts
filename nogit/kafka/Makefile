SHELL=/bin/bash
PATH := .venv/bin:$(PATH)
# pip install Cython; \
# pip install numpy cython; \
# pip install --no-binary :all: --no-use-pep517 numpy; \
# pip install pandas; \
# pip install ib_insync; \

install:
	@[ ! -d .venv ] && python3 -m venv --copies .venv ||:;
	@( \
		source .venv/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements.txt; \
	)

mypy:
	@mypy src;

lint: mypy black isort autoflake

lint-fix: #mypy
	@black --exclude '.venv|build|target|dist|.cache|node_modules' .;
	@isort -q -l=250 --force-single-line-imports .;
	@autoflake --in-place --recursive --exclude '.venv,build,target,dist,.cache,node_modules' --remove-all-unused-imports --remove-unused-variables .;
	@isort -q .;