import sys
import datetime
import re
from os import walk, mkdir
from os.path import join, dirname, realpath, relpath, exists

from jinja2 import Environment, FileSystemLoader

from ocdev.plugins.validators import RegexValidator
from ocdev.plugins.plugin import Plugin


class Author:

    def __init__(self, name, email, homepage=''):
        self.name = name
        self.email = email
        self.homepage = homepage


class Arguments:

    def __init__(self, name, description='', license='agpl', owncloud='7.0.3',
                 version='0.0.1', authors=[], output=''):
        self.authors = authors
        self.name = name
        self.description = description
        self.license = license
        self.owncloud = owncloud
        self.version = version
        self.output = output
        self.attrs = ['authors', 'name', 'description', 'license', 'owncloud',
                      'version']

    def __contains__(self, item):
        if item in self.attrs:
            return True
        else:
            return False


class StartApp(Plugin):

    def __init__(self):
        super().__init__('startapp')


    def add_sub_parser(self, main_parser):
        parser = main_parser.add_parser('startapp', help='Create an app')
        parser.set_defaults(which='startapp')

        parser.add_argument('--author', help='Author\'s name', required=True)
        parser.add_argument('--mail', help='Author\'s E-Mail', required=True)
        parser.add_argument('--description', help='Whether license headers \
                            should be included in every file', default='')
        parser.add_argument('--homepage', help='Author\'s homepage', default='')
        parser.add_argument('--license', help='The app license', default='agpl',
                            choices=['agpl', 'mit'])
        parser.add_argument('--owncloud', help='Required ownCloud version',
                            default='7.0.3')
        parser.add_argument('--version', help='App version', default='0.0.1')
        parser.add_argument('--output', help='Output generated files into \
                            this directory instead of the current one if given',
                            default='')
        parser.add_argument('name', help='Name of the app in camel case \
                            e.g. MyApp', type=RegexValidator('^([A-Z][a-z]+)+$',
                            'Must be camel case e.g. MyApp'))


    def run(self, arguments, directory):
        # overwrite default path if argument given
        if arguments.output != '':
            directory = arguments.output

        current_dir = dirname(realpath(__file__))
        template_dir = join(current_dir, 'templates')

        # choose the appropriate version for the app templates that is determined
        # by the owncloud minimum version
        app_dir = '%s/app' % arguments.owncloud.split('.')[0]
        app_template_dir = join(template_dir, app_dir)

        # if author is given its being run from commandline and the list has to
        # be assembled first
        if 'author' in arguments:
            authors = [{
                'name': arguments.author,
                'email': arguments.mail,
                'homepage': arguments.homepage
            }]
        else:
            authors = arguments.authors

        # get licenses
        small_license_header = 'includes/licenses/%s.header.php' % arguments.license
        full_license = 'includes/licenses/%s.txt' % arguments.license

        params = {
            'app': {
                'id': arguments.name.lower(),
                'name': ' '.join(re.findall(r'[A-Z][^A-Z]*', arguments.name)),
                'description': arguments.description,
                'license': arguments.license,
                'owncloud_version': arguments.owncloud,
                'version': arguments.version,
                'namespace': arguments.name,
                'small_license_header': small_license_header,
                'full_license': full_license,
                'authors': authors
            },
            'date': {
                'year': datetime.date.today().year
            }
        }

        env = Environment(loader=FileSystemLoader(template_dir))

        # create app directory
        app_dir = join(directory, params['app']['id'])
        if exists(app_dir):
            print('Can not create app, directory %s exists already' % app_dir)
            sys.exit(1)

        mkdir(app_dir)

        # create folders and files in that directory
        for root, dirs, files in walk(app_template_dir):

            # folders first
            for folder in dirs:
                abs_path = join(root, folder)
                destination = join(app_dir, relpath(abs_path, app_template_dir))
                mkdir(destination)

            # then read the templates and create the parsed files
            for file in files:
                abs_path = join(root, file)
                jinja_path = relpath(abs_path, template_dir)
                destination = join(app_dir, relpath(abs_path, app_template_dir))

                rendered = env.get_template(jinja_path).render(params)

                with open(destination, 'w+') as f:
                    f.write(rendered)
