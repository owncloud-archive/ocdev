# ownCloud developer tools
This is a Python 3 library. Every pip and python command in the following code
samples should be, if needed, replaced by the appropriate command on your system (e.g. python3, pip3)

## Installation

To install it run:

    sudo pip install -r requirements.txt
    sudo python setup.py install

You can also install it from pypi by running:

    sudo pip install ocdev

## Creating apps

To create an app in the current directory:

    ocdev startapp --author Bernhard Posselt --mail dev@bernhard-posselt.com MyApp

The following optional commandline options are available:

* **--version**: defaults to 0.0.1
* **--description**: sets the app description in the appinfo/info.xml
* **--homepage**: sets the author's homepage in the AUTHORS.md file
* **--license**: agpl or mit, defaults to agpl
* **--owncloud**: the minimum ownCloud version, defaults to 6.0.3

For a more verbose output run:

    ocdev startapp -h

## Interfacing with the generator
To use the app generator in your python app use:

```python
from ocdev.plugins.startapp.startapp import StartApp, Author, Arguments

author = Author(name='Bernhard Posselt', email='dev@bernhard-posselt.com', 
                homepage='http://bernhard-posselt.com')

arguments = Arguments(name='MyApp', 
                      description='My App Yeah!',    # defaults to ''
                      owncloud='6.0.3',              # defaults to '6.0.3'
                      version='0.0.1',               # defaults to '0.0.1'
                      authors=[author],              # defaults to []
                      license='mit',                 # defaults to agpl
            )

write_directory = '/srv/http/owncloud/apps/'

app = StartApp()
app.run(arguments, write_directory)
```