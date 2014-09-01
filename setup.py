from setuptools import setup, find_packages

with open('requirements.txt', 'r') as infile:
    install_requires = infile.read().split('\n')

with open('README.rst', 'r') as infile:
    long_description = infile.read()

setup (
    name = 'ocdev',
    version = '0.0.14',
    description = 'ownCloud development tool',
    long_description = long_description,
    author = 'Bernhard Posselt',
    author_email = 'dev@bernhard-posselt.com',
    url = 'https://github.com/Raydiation/ocdev',
    packages = find_packages(),
    include_package_data = True,
    license = 'GPL',
    install_requires = install_requires,
    keywords = ['owncloud', 'app', 'scaffolding', 'setup', 'development'],
    entry_points = {
        'console_scripts': [
            'ocdev = ocdev.application:main'
        ]
    }
)
