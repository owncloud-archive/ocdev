from os.path import join, dirname, realpath, relpath, exists
from subprocess import call

from jinja2 import Environment, FileSystemLoader

from ocdev.plugins.plugin import Plugin


class Arguments:

    def __construct__(self, db='sqlite'):
        self.db = db


class ContinousIntegration(Plugin):

    def __init__(self):
        super().__init__('ci')


    def add_sub_parser(self, main_parser):
        parser = main_parser.add_parser('ci', help='Sets up ownCloud install \
                                        for running the continuous integration \
                                        tests')
        parser.set_defaults(which='ci')

        parser.add_argument('db', help='Sets the database', default='sqlite',
                            choices=['mysql', 'sqlite', 'postgresql'])


    def run(self, arguments, directory):
        current_dir = dirname(realpath(__file__))
        template_dir = join(current_dir, 'templates')

        params = {
            'admin': {
                'user': 'admin',
                'password': 'admin'
            },
            'data': join(directory, 'data'),
            'database': {
                'user': 'oc_autotest',
                'password': '',
                'name': 'oc_autotest',
                'host': 'localhost',
            }
        }

        env = Environment(loader=FileSystemLoader(template_dir))

        autoconfig = '/autoconfig/%s.php' % arguments.db
        rendered = env.get_template(autoconfig).render(params)

        with open('tests/preseed-config.php', 'r') as preseed:
            with open('config/config.php', 'w') as config:
                config.write('%s\nDEFINE("DEBUG", true);' % preseed.read())

        with open('config/autoconfig.php', 'w') as f:
            f.write(rendered)

        call(['php', '-f', 'index.php'])
