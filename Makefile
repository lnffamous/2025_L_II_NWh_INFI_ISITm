# 1. Instaluje zależności programu i testów
deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt

# 2. Uruchamia linter (flake8)
lint:
	flake8 .

# 3. Uruchamia testy jednostkowe (używamy pytest, bo masz test_requirements.txt)
test:
	pytest

# 4. Uruchomienie aplikacji (bazując na main.py)
run:
	python3 main.py
