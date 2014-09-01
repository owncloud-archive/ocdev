all: install

install: clean
	sudo python3 setup.py install

uninstall: clean
	sudo rm -rf /usr/lib/python3.4/site-packages/ocdev*
	sudo rm -rf /usr/bin/ocdev

clean:
	sudo rm -rf dist
	sudo rm -rf MANIFEST
	sudo rm -rf build
	sudo rm -rf ocdev.egg-info

pypi: clean
	python setup.py sdist upload
