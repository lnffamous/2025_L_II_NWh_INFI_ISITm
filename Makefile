deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt
	
lint:
	python -m flake8 hello_world test
	
run:
	python main.py
	
.PHONY: test
test: lint
	PYTHONPATH=. py.test --verbose -s
docker_build:
	docker build -t hello-world-printer-isit .
docker_run: docker_build
	docker run \
		--name hello-world-printer-dev \
		-p 5000:5000 \
		-d hello-world-printer-isit
TAG=$(USERNAME)/hello-world-printer-isit
docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag hello-world-printer-isit $(TAG); \
	docker push $(TAG); \
	docker logout;
