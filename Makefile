.DEFAULT_GOAL := all

.PHONY: all
all: clean

.PHONY: clean
clean:
	-rm	-rf	./build/
	-rm	-rf	./dist/
	-rm	-rf	logs
	-rm	-rf	report

.PHONY: test
test:
	pytest