from subprocess import check_call

from ocdev.plugins.plugin import Plugin

class Server(Plugin):

    def __init__(self):
        super().__init__('server')


    def add_sub_parser(self, main_parser):
        parser = main_parser.add_parser('server', help='Server')
        parser.set_defaults(which='server')

        parser.add_argument('--port', help='Server port', default='8080')


    def run(self, arguments, directory, settings):
        check_call(['php', '-S', 'localhost:%s' % arguments.port])