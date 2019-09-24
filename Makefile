pip=env/bin/python -m pip
projector=../env/bin/projector

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
# 	cd tests && python test.py
	rm -rf test_empty && mkdir test_empty && cd test_empty && $(projector) build

.PHONY: all configure test lint build install
