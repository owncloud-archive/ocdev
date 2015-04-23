from subprocess import check_call
from os.path import isfile, join
from os import listdir, chdir

from ocdev.plugins.plugin import Plugin
from ocdev.plugins.pluginerror import PluginError

class DevUp(Plugin):

    def __init__(self):
        super().__init__('devup')


    def add_sub_parser(self, main_parser):
        parser = main_parser.add_parser('devup', help='Recursively your core \
                                                       and apps using git')
        parser.set_defaults(which='devup')

        parser.add_argument('--branch', help='Preferred branch for core and apps',
                                        default='master')
        parser.add_argument('dir', help='Path to core, defaults to the current \
                                         folder', default='', nargs='?')


    def run(self, arguments, directory, settings):
        if arguments.dir != '':
            directory = arguments.dir

        if not isfile(join(directory, 'config/config.php')):
            raise PluginError('ownCloud core directory not found in path %s' %directory)

        chdir(directory)

        git_rebase = ['git', 'pull', '--rebase', 'origin', arguments.branch]

        check_call(git_rebase)

        for dir in listdir(directory):
            print(dir)