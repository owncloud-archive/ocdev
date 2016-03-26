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

    def __init__(self, name, description='', license='agpl', owncloud='9.0',
                 version='0.0.1', authors=[], output='', category='multimedia'):
        self.authors = authors
        self.name = name
        self.description = description
        self.license = license
        self.owncloud = owncloud
        self.version = version
        self.output = output
        self.attrs = ['authors', 'name', 'description', 'license', 'owncloud',
                      'version', 'category']

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

        parser.add_argument('--author', help='Author\'s name')
        parser.add_argument('--email', help='Author\'s E-Mail')
        parser.add_argument('--description', help='Whether license headers \
                            should be included in every file',
                            default='My first ownCloud app')
        parser.add_argument('--homepage', help='Author\'s homepage', default='')
        parser.add_argument('--license', help='The app license', default='agpl',
                            choices=['agpl', 'mit'])
        parser.add_argument('--category', help='The app category',
                            default='other',
                            choices=['multimedia', 'tool', 'pim', 'other',
                                     'game', 'productivity'])
        parser.add_argument('--owncloud', help='Required ownCloud version',
                            default='9.0')
        parser.add_argument('--version', help='App version', default='0.0.1')
        parser.add_argument('--output', help='Output generated files into \
                            this directory instead of the current one if given',
                            default='')
        parser.add_argument('name', help='Name of the app in camel case \
                            e.g. MyApp', type=RegexValidator('^([A-Z][a-z]+)+$',
                            'The app name must be camel case e.g. MyApp'))


    def run(self, arguments, directory, settings):
        # overwrite default path if argument given
        if arguments.output != '':
            directory = arguments.output

        current_dir = dirname(realpath(__file__))
        template_dir = join(current_dir, 'templates')

        # choose the appropriate version for the app templates that is determined
        # by the owncloud minimum version
        owncloud_version = arguments.owncloud.split('.')

        # owncloud 8 has a new versioning scheme where we need more than one
        # number
        if int(owncloud_version[0]) < 8:
            owncloud_version = owncloud_version[0]
        else:
            # in case a user enters 8 instead of 8.0
            if len(owncloud_version) == 1:
                owncloud_version.append('0')
            owncloud_version = '%s.%s' % (owncloud_version[0],
                                          owncloud_version[1])

        app_dir = '%s/app' % owncloud_version
        app_template_dir = join(template_dir, app_dir)

        # if author is given its being run from commandline and the list has to
        # be assembled first
        if 'authors' in arguments:
            authors = arguments.authors
        else:
            authors = []
            author =  {}
            for key, tmpl_name in zip(['author', 'email'], ['name', 'email']):
                if key in arguments and getattr(arguments, key):
                    author[tmpl_name] = getattr(arguments, key)
                else:
                    author[tmpl_name] = settings.get_value('startapp', key)
            authors.append(author)

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
                'authors': authors,
                'category': arguments.category
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
                jinja_path = relpath(abs_path, template_dir).replace('\\', '/')
                destination = join(app_dir, relpath(abs_path, app_template_dir))

                rendered = env.get_template(jinja_path).render(params)

                with open(destination, 'w+') as f:
                    f.write(rendered)
