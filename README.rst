ownCloud developer tools
========================
To install it run::

	sudo python3 setup.py install

You can also install it from pypi by running::

	sudo pip install ocdev

Creating apps
-------------
To create an app in the current directory::

	ocdev startapp --author Bernhard Posselt --mail dev@bernhard-posselt.com MyApp

The following optional commandline options are available:

* **--version**: defaults to 0.0.1
* **--description**: sets the app description in the appinfo/info.xml
* **--homepage**: sets the author's homepage in the AUTHORS.md file
* **--license**: agpl or mit, defaults to agpl
* **--owncloud**: the minimum ownCloud version, defaults to 6.0.3

For a more verbose output run:

    ocdev startapp -h

