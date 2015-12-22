from setuptools import setup, find_packages

with open('requirements.txt', 'r') as infile:
    install_requires = infile.read().split('\n')

with open('README.rst', 'r') as infile:
    long_description = infile.read()

with open("ocdev/version.txt", 'r') as infile:
    version = ''.join(infile.read().split())

setup (
    name = 'ocdev',
    version = version,
    description = 'ownCloud development tool',
    long_description = long_description,
    author = 'Bernhard Posselt',
    author_email = 'dev@bernhard-posselt.com',
    url = 'https://github.com/owncloud/ocdev',
    packages = find_packages(exclude=('tests',)),
    include_package_data = True,
    license = 'GPL',
    install_requires = install_requires,
    keywords = ['owncloud', 'app', 'scaffolding', 'setup', 'development'],
    test_suite = 'tests',
    classifiers = [
        'Classifier: Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Code Generators'
    ],
    entry_points = {
        'console_scripts': [
            'ocdev = ocdev.application:main'
        ]
    }
)
