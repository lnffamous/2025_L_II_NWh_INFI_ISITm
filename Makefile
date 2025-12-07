.PHONY: lint test

lint:
	flake8 hello_world

test: lint
	PYTHONPATH=. py.test --verbose -s

run:
	python main.py

