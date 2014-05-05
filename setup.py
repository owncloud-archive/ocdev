from setuptools import setup, find_packages

setup (
    name = 'ocdev',
    version = '0.0.3',
    description = 'ownCloud development tool',
    long_description=open('README.rst').read()
    author = 'Bernhard Posselt',
    author_email = 'dev@bernhard-posselt.com',
    url = 'https://github.com/Raydiation/ocdev',
    packages = find_packages(),
    include_package_data = True,
    license = 'GPL',
    install_requires = ['jinja2'],
    keywords = ['owncloud', 'app', 'scaffolding', 'setup', 'development'],
    entry_points = {
        'console_scripts': [
            'ocdev = ocdev.application:main'
        ]
    }
)
