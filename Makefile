.DEFAULT_GOAL := all

.PHONY: all
all: clean build

.PHONY: clean
clean:
	-rm	-rf	./build/
	-rm	-rf	./dist/
	-rm	-rf	logs
	-rm	-rf	report

.PHONY: test
test:
	pytest

.PHONY: install
install:
	python setup.py install

.PHONY: uninstall
uninstall:
	pip uninstall ist -y

.PHONY: reinstall
reinstall: uninstall install

.PHONY: build
build:
	docker build -t ist:0.1.0 .

.PHONY: run
run:
	docker run -v ./config.ini:/app/config.ini ist:0.1.0