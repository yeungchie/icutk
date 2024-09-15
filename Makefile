.PHONY: tests

PY=python3

check:
	$(PY) -m ruff check ./icutils

make tests:
	$(PY) -m pytest -v ./tests

clean:
	find ./icutils ./tests -type d -name __pycache__ -exec rm -rf {} +
	rm -rf build
	rm -rf dist
	rm -rf icutils.egg-info

install:
	$(PY) -m pip install .

uninstall:
	$(PY) -m pip uninstall icutils -y
	
build:
	make clean
	$(PY) setup.py sdist build

upload: dist
	$(PY) -m twine upload dist/*
