import os
import stat
from subprocess import call

from ocdev.plugins.plugin import Plugin


class Arguments:

    def __construct__(self, level='core', branch='master', type='https',
                      directory='core'):
        self.level = level
        self.branch = branch
        self.type = type
        self.dir = directory


class SetUp(Plugin):

    def __init__(self):
        super().__init__('setup')
        

    def add_sub_parser(self, main_parser):
        parser = main_parser.add_parser('setup', help='Setup ')
        parser.set_defaults(which='setup')

        parser.add_argument('--type', help='If SSH or HTTPS should be used to \
                            fetch the sources. Defaults to HTTPS since you need \
                            push access in order to use SSH', default='https',
                            choices=['https', 'ssh'])
        parser.add_argument('--branch', help='The branch which should be \
                            checked out', default='master')
        parser.add_argument('--dir', help='The directory name, defaults to core',
                            default='core')
        parser.add_argument('level', help='core or base. core only sets up \
                            a working core setup, base also installs apps like \
                            news, notes, calendar, gallery, music, documents \
                            and contacts', choices=['core', 'base'], 
                            default='core')


    def run(self, arguments, directory):
        urls = {
            'ssh': {
                'core': 'git@github.com:owncloud/core.git',
                'apps': [
                    'git@github.com:owncloud/news.git',
                    'git@github.com:owncloud/gallery.git',
                    'git@github.com:owncloud/music.git',
                    'git@github.com:owncloud/notes.git',
                    'git@github.com:owncloud/calendar.git',
                    'git@github.com:owncloud/contacts.git',
                    'git@github.com:owncloud/documents.git',
                    'git@github.com:owncloud/chat.git',
                    'git@github.com:owncloud/bookmarks.git'
                ]
            },
            'https': {
                'core': 'https://github.com/owncloud/core.git',
                'apps': [
                    'https://github.com/owncloud/news.git',
                    'https://github.com/owncloud/gallery.git',
                    'https://github.com/owncloud/music.git',
                    'https://github.com/owncloud/notes.git',
                    'https://github.com/owncloud/calendar.git',
                    'https://github.com/owncloud/contacts.git',
                    'https://github.com/owncloud/documents.git',
                    'https://github.com/owncloud/chat.git',
                    'https://github.com/owncloud/bookmarks.git'
                ]
            }
        }

        chosen_urls = urls[arguments.type]

        # check if directory is writeable
        if os.access(directory, os.W_OK):
            code = call(['git', 'clone', '-b', arguments.branch, 
                        chosen_urls['core'], arguments.dir])
            
            if code != 0:  # default to master if branch fails
                call(['git', 'clone', '-b', 'master', chosen_urls['core'], 
                     arguments.dir])

            os.chdir(arguments.dir)
            call(['git', 'submodule', 'init'])
            call(['git', 'submodule', 'update'])
            
            os.chdir('3rdparty')
            call(['git', 'checkout', arguments.branch])
            os.chdir('..')

            os.mkdir('data')

            # make config/ read and writeable to run the setup
            os.chmod('config', os.stat('config').st_mode
                     | stat.S_IXOTH   # a+x
                     | stat.S_IROTH   # a+r
                     | stat.S_IWOTH)  # a+w

            os.chmod('apps', os.stat('apps').st_mode
                     | stat.S_IWOTH)  # a+w

            if arguments.level == 'base':
                os.chdir('apps')
                for app_url in chosen_urls['apps']:
                    # repository might not have that specific branch, in that 
                    # case just take master
                    code = call(['git', 'clone', '-b', arguments.branch, app_url])
                    if code != 0:
                        code = call(['git', 'clone', '-b', 'master', app_url])

            print('\nSuccessfully set up development environment!')
            print('To run the setup you will need to change the group and owner')
            print('of the data directory to be owned by your webserver user and')
            print('group (http in this case, otherwise apache, www-data or httpd):')
            print('\n    sudo chown -R http:http %s/data\n' % arguments.dir)

        else:
            print('Can not write to directory %s. Aborted' % directory)
