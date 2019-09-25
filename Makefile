pip=env/bin/python -m pip
python=env/bin/python3
projector=env/bin/projector

all: install

lint:
	@poetry check
	@flake8

configure:
	@poetry install

build: 
	@poetry build
	@rm -rf env
	@python -m venv env

install: build
	$(pip) install dist/projector*.whl

test: install
	# script test
	rm -rf test_empty && mkdir test_empty && cd test_empty && ../$(projector) build test_open_folder
	cd test_empty && ../$(projector) run
	# unittests doesn't work yet
# 	cd tests && ../$(python) test.py


.PHONY: all configure test lint build install
