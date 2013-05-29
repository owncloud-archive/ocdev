ownCloud scaffolder
===================
To install it run::

	sudo python setup.py install

You can also install it from pypi by running::

	sudo pip install owncloud_scaffolding

Usage
-----
To create an app in the current directory::

	owncloud.py startapp my_app_name

It will prompt for more information on metadata.

To change the template directory use::

	owncloud.py --templates PATH/TO/DIRECTORY startapp my_app_name

It's also possible to omit the license headers by using::
	
	owncloud.py startapp --headers False my_app_name