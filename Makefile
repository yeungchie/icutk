.PHONY: check tests clean install uninstall build

PY=python3

check:
	$(PY) -m ruff check ./icutk

tests:
	$(PY) -m pytest -v ./tests

clean:
	find ./ -type d -name __pycache__ -exec rm -rf {} +
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

install:
	$(PY) -m pip install .

uninstall:
	$(PY) -m pip uninstall icutk -y

build:
	make clean
	$(PY) setup.py build sdist bdist_wheel

upload: dist
	$(PY) -m twine upload dist/*
