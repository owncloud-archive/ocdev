========================
ownCloud developer tools
========================

.. image:: https://travis-ci.org/owncloud/ocdev.svg
    :target: https://travis-ci.org/owncloud/ocdev

This is a Python 3 library. Every pip and python command in the following code
samples should be, if needed, replaced by the appropriate command on your system (e.g. python3, pip3)

**Developer Info:**

To test your changes locally without globally installing the tool on your machine run::

    python3 -m ocdev COMMAND

inside the cloned folder.

The **-m** option tells python to run the **ocdev/__main__.py** file. This is needed to have working imports in both installed and local versions.

.. note:: If the library is also installed the installed version imports will be used and local changes will be ignored. **Make sure to uninstall the global version first before running the local version**!

Installation
============
If **Python 3** and **pip** are not yet installed on the system, install it from your package manager, e.g.::

    sudo apt-get install python3 python3-pip

Verify the Python version using::

    python --version

If it outputs **Python 3.2 or lower** (e.g. on **Ubuntu 12.04**) you will **need to install jinja from your package manager first**, e.g.::

    sudo apt-get install python3-jinja2

Then install the tool::

    sudo pip-3.2 install ocdev

For the **setup** command, **git** has to be installed.

Updating
========
To update the library run::

    sudo pip-3.2 install --upgrade ocdev


Get the currently installed version
===================================

To get the currently active version run::

    ocdev --version

Setting up a development environment
====================================
To set up your development environment run::

    ocdev setup core

or::

    ocdev setup base

If you use **base** the following additional apps will be installed:

* activity
* bookmarks
* calendar
* chat
* contacts
* documents
* gallery
* music
* notes
* news

If at least **core** is set up, you can use::

    ocdev setup <repositoryname>

to clone a repository from ownCloud organization. To see all available
repositories, click [here](https://github.com/owncloud).

The following optional commandline options are available:

* **--dir**: sets the name of the owncloud directory, defaults to core/
* **--branch**: sets the branch which should be cloned, defaults to master
* **--type**: sets the type that should be cloned, ssh or https. Defaults to https since you need access to the repository to use ssh

For a more verbose output run::

    ocdev setup -h

Creating apps
=============

To create an app in the current directory::

    ocdev startapp --author "Bernhard Posselt" --mail dev@bernhard-posselt.com MyApp

The following optional commandline options are available:

* **--version**: defaults to 0.0.1
* **--description**: sets the app description in the appinfo/info.xml
* **--homepage**: sets the author's homepage in the AUTHORS.md file
* **--license**: agpl or mit, defaults to agpl
* **--owncloud**: the minimum ownCloud version, defaults to the currently active version
* **--output**: The directory where the generated files should be written to. Defaults to the current directory

For a more verbose output run::

    ocdev startapp -h


Setting up a test instance for continuous integration
====================================================
To set up a test instance for continuous integration (e.g. on Travis-CI) run::

    ocdev setup core
    cd core
    ocdev ci mysql

The following databases can be chosen:

* **mysql**
* **sqlite**
* **postgresql**

The script requires php to be available from commandline.

Interfacing with the app generator
==================================
To use the app generator in your python app use::

Setting up development environment
----------------------------------

.. code:: python

  from ocdev.plugins.setup.setup import SetUp, Arguments

  arguments = Arguments(level='base',          # defaults to 'core'
                        branch='stable6',      # defaults to 'master'
                        type='ssh',            # defaults to 'https'
                        directory='owncloud'   # defaults to 'core'
              )

  write_directory = '/srv/http/owncloud/apps/'

  app = SetUp()
  app.run(arguments, write_directory)


Creating apps
-------------

.. code:: python

  from ocdev.plugins.startapp.startapp import StartApp, Author, Arguments

  author = Author(name='Bernhard Posselt', email='dev@bernhard-posselt.com',
                  homepage='http://bernhard-posselt.com')

  arguments = Arguments(name='MyApp',
                        description='My App Yeah!',    # defaults to ''
                        license='mit',                 # defaults to 'agpl'
                        owncloud='6.0.3',              # defaults to '6.0.3'
                        version='0.0.1',               # defaults to '0.0.1'
                        authors=[author],              # defaults to []
              )

  write_directory = '/srv/http/owncloud/apps/'

  app = StartApp()
  app.run(arguments, write_directory)


Setting up a test instance for continuous integration
----------------------------------------------------


.. code:: python

  from ocdev.plugins.ci.ci import ContinousIntegration, Arguments

  arguments = Arguments(db='sqlite')  # 'mysql', 'postgresql', 'sqlite'


  write_directory = '/srv/http/owncloud/apps/'

  app = ContinousIntegration()
  app.run(arguments, write_directory)
