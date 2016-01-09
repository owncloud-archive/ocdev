ocdev (0.2.0)

* Add ownCloud 8.2 templates and set as default when generating apps
* Check for Python 2 on install to prevent being install with the wrong pip version


ocdev (0.1.8)

* Also run git fetch before checking out the branch to make sure that branch updates work
* Remove non working appstore upload command from makefiles

ocdev (0.1.7)

* 8.1 travis ci fixes

ocdev (0.1.6)

* Updates for the 8.1 templates

ocdev (0.1.4)

* Add ocdev devup command to easily update your install

ocdev (0.1.3)

* Allow to set the preferred type of cloning in the .ocdevrc file
* Make ocdev ready for 8.1

ocdev (0.1.2)

* Add a --no-history flag to the setup command to pass depth 1 to git clone for faster cloning on ci servers

ocdev (0.1.1)

* Fix travis.yml for ownCloud 8 apps
* Add an ocdev server command as a php server shortcut

ocdev (0.1.0)

* Add a Makefile for ownCloud 8 apps to build an app package and upload the app to the app store
* Add a configuration file ~/.ocdevrc where often used settings are saved
* Rename the --mail paramter to --email for the startapp command
* Add a --category parameter to the startapp command
* Default to owncloud 8 as minimum level when creating apps
* Do not create a data directory since this is done automatically by ownCloud
* Remove the chown hints when setting up ownCloud since the PHP built in development server should be preferred
* Add integration test phpunit configuration for ownCloud 8 apps and move autoloader to unit test directory
* Add an integration test ready travis.yml for ownCloud 8 apps

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
