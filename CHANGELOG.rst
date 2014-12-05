ocdev (0.1.0)

* Add the possibility to release and update an app on the app store
* Add Makefile for ownCloud 8 to build an app package and upload the app to the app store
* Add a configuration file ~/.ocdevrc where often used settings are saved
* Rename the --mail paramter to --email for the startapp command
* Add a --category parameter to the startapp command

ocdev (0.0.19)

* Switch version to shorter ocdev --version

ocdev (0.0.18)

* Keep version in ocdev/version.txt and provide an ocdev version command to get the current version

ocdev (0.0.17)

* Remove app creation for ownCloud 6 since there are no dev docs, 7 is recommended
* Bump default required ownCloud version to 7.0.3 since the package built with the makefile relies on bugfixes in core
* Support ownCloud 8

ocdev (0.0.16)

* use absolute path for datadirectory when running the ocdev ci command

ocdev (0.0.15)

* Add support to clone specific repositories from ownCloud organization on GitHub
* Activity app is also now part of base environment

ocdev (0.0.14)

* Fix unit tests on PHP 5.3

ocdev (0.0.13)

* Fix broken unit test
* Add navigation, settings and content html basic structure

ocdev (0.0.12)

* Uppercase License Acronym in info.xml
* Fail nicely if Git is not installed when running the setup command
* Provide optional output parameter for startapp command

ocdev (0.0.11)

* Several minor fixes

ocdev (0.0.10)

* Fix ci

ocdev (0.0.9)

* Fix setup problems on mysql & postgresql

ocdev (0.0.8)

* Add **DEFINE('DEBUG', true);** to autoconfigs

ocdev (0.0.7)

* Disable enabling of files_sharing, files_encryption, files_external, user_ldap and files_versions apps since they might not be needed and can be activated by php -f console.php app:enable files_versions for instance

ocdev (0.0.6)

* Add generator for ci setups that generates configs for core and setups an install for tests

ocdev (0.0.5)

* Add templates for ownCloud 7

ocdev (0.0.4)

* Move to setuptools for distributing
* Fail more gracefully if app directory exists already
* Transition to reST documentation files

ocdev (0.0.3)

* Fix bug that breaks calling ocdev setup base


ocdev (0.0.2)

* Add support for setting up the development environment


ocdev (0.0.1)

* First release
