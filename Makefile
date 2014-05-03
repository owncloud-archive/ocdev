all: install

install: clean
	sudo python setup.py install

clean:
	rm -rf dist
	rm -rf MANIFEST
	sudo rm -rf build

pypi: clean
	python setup.py sdist upload
