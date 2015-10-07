=========================
ownCloud development tool
=========================

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

Linux Installation
===================

**Install Python**

If **Python 3** and **pip** are not yet installed on the system, install it from your package manager, e.g.::

    sudo apt-get install python3 python3-pip

Verify the Python version using::

    python --version

If it outputs **Python 3.2 or lower** (e.g. on **Ubuntu 12.04**) you will **need to install jinja from your package manager first**, e.g.::

    sudo apt-get install python3-jinja2

**Install the ocdev tool**

    sudo pip3 install ocdev

Windows Installation
====================

**Install Python**

Download latest Python v3 for Windows from https://www.python.org/downloads/ and start installation. Select custom installation and check add PATH variables. **Do not install Python for all users**, this will cause errors when running the script because of access restrictions to windows program folders.

**Install the ocdev tool**

Open the windows command line (CLI) and type::

    pip install ocdev

Updating
========
To update the library run::

    sudo pip3 install --upgrade ocdev


Get the currently installed version
===================================

To get the currently active version run::

    ocdev --version


Configuration file
==================
After running ocdev for the first time a new config file called **.ocdevrc** will be created in your home directory and can contain the following values:

.. code:: ini

    [setup]
    type = https

    [startapp]
    email = your@mail.com
    homepage = your-website.com
    author = John Doe

    [appstore]
    url = https://api.owncloud.com/v1
    user = john_doe
    password = john_does_password

    [devup]
    core = master


Setting up a development environment
====================================
To set up your development environment run

(for the setup command, **git** must be available on your machine. Git can be installed with *apt-get install git* or downloaded from https://git-for-windows.github.io/ for windows)::

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
repositories, click `here <https://github.com/owncloud/>`_

The following optional commandline options are available:

* **--dir**: sets the name of the owncloud directory, defaults to core/
* **--branch**: sets the branch which should be cloned, defaults to master
* **--type**: sets the type that should be cloned, ssh or https. Defaults to https since you need access to the repository to use ssh

For a more verbose output run::

    ocdev setup -h

Creating apps
=============

To create an app in the current directory::

    ocdev startapp MyApp

The following optional commandline options are available:

* **--author**: If not given will be read from ~/.ocdevrc or queried on the command line
* **--email**: If not given will be read from ~/.ocdevrc or queried on the command line
* **--version**: defaults to 0.0.1
* **--description**: sets the app description in the appinfo/info.xml
* **--homepage**: sets the author's homepage in the AUTHORS.md file
* **--license**: agpl or mit, defaults to agpl
* **--owncloud**: the minimum ownCloud version, defaults to the currently active version
* **--no-history**: if given, clones with depth 1 which is very fast and clones only the current status. This is not suited for development but may be desirable on your continuous integration server.
* **--output**: The directory where the generated files should be written to. Defaults to the current directory

For a more verbose output run::

    ocdev startapp -h


Starting a PHP development server
=================================
To run a PHP dev server you can run::

    php -S localhost:8080

ocdev provides a shortcut for this common task::

    ocdev server

The following optional commandline options are available:

* **--port**: defaults to 8080

Updating development environments
=================================
Sometimes it tedious to keep your installation up to date. To update all the apps to the newest commit in a branch you can use ocdev devup::

    ocdev devup /path/to/core

If the path is ommited, the current directory will be chosen.

Only apps defined in your ~/.ocdevrc, including core will be updated. They need to be listed in the following format:

.. code:: ini

    [devup]
    app = branch

e.g.:

.. code:: ini

    [devup]
    core = master
    news = dev
    calendar = stable8


Setting up a test instance for continuous integration
=====================================================

.. note:: Deprecated in ownCloud 8.1, use the occ install command, e.g.:

  ./occ maintenance:install --database-name oc_autotest --database-user oc_autotest --admin-user admin --admin-pass admin --database-pass --database (pgsql|mysql|sqlite)

To set up a test instance for continuous integration (e.g. on Travis-CI) run::

    ocdev setup core
    cd core
    ocdev ci mysql

The following databases can be chosen:

* **mysql**
* **sqlite**
* **postgresql**

The script requires php to be available from commandline.
