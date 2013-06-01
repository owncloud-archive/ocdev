ownCloud scaffolder
===================
To install it run::

	sudo python3 setup.py install

You can also install it from pypi by running::

	sudo pip install owncloud_scaffolding

Creating apps
-------------
To create an app in the current directory::

	owncloud.py startapp my_app_name

It will prompt for more information on metadata.

To change the template directory use::

	owncloud.py --templates PATH/TO/DIRECTORY startapp my_app_name

It's also possible to omit the license headers by using::

	owncloud.py startapp --headers False my_app_name

If you wish to create a classic app without the App Framework use::

	owncloud.py startapp --type classic my_app_name


Creating resources
--------------------
A resource consists of an entity, a mapper, a service layer and a controller

To create a resource and test in the current directory::

	owncloud.py resource name
