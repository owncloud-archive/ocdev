from ocdev.plugins.plugin import Plugin
from ocdev.version import get_version

class Version(Plugin):

    def __init__(self):
        super().__init__('version')


    def add_sub_parser(self, main_parser):
        parser = main_parser.add_parser('version',
                                        help='Print out the ocdev version')
        parser.set_defaults(which='version')


    def run(self, arguments, directory):
        print(get_version())
