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
                'apps': {
                    'news': 'git@github.com:owncloud/news.git',
                    'gallery': 'git@github.com:owncloud/gallery.git',
                    'music': 'git@github.com:owncloud/music.git',
                    'notes': 'git@github.com:owncloud/notes.git',
                    'calendar': 'git@github.com:owncloud/calendar.git',
                    'contacts': 'git@github.com:owncloud/contacts.git',
                    'documents': 'git@github.com:owncloud/documents.git',
                    'chat': 'git@github.com:owncloud/chat.git',
                    'bookmarks': 'git@github.com:owncloud/bookmarks.git'
                }
            },
            'https': {
                'core': 'https://github.com/owncloud/core.git',
                'apps': {
                    'news': 'https://github.com/owncloud/news.git',
                    'gallery': 'https://github.com/owncloud/gallery.git',
                    'music': 'https://github.com/owncloud/music.git',
                    'notes': 'https://github.com/owncloud/notes.git',
                    'calendar': 'https://github.com/owncloud/calendar.git',
                    'contacts': 'https://github.com/owncloud/contacts.git',
                    'documents': 'https://github.com/owncloud/documents.git',
                    'chat': 'https://github.com/owncloud/chat.git',
                    'bookmarks': 'https://github.com/owncloud/bookmarks.git'
                }
            }
        }

        chosen_urls = urls[arguments.type]

        # check if directory is writeable
        if os.access(directory, os.W_OK):
            call(['git', 'clone', '-b', arguments.branch, chosen_urls['core'],
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
