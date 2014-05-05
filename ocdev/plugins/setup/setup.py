import os
from subprocess import call

from plugins.plugin import Plugin


class Arguments:

    def __construct__(self, level='core', branch='master', type='https'):
        self.level = level
        self.branch = branch
        self.type = type


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
        parser.add_argument('level', help='core or base. core only sets up \
                            a working core setup, base also installs apps like \
                            news, notes, calendar, gallery, music, documents \
                            and contacts',
                            choices=['core', 'base'])


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
            call(['git' 'clone ', '-b', arguments.branch, chosen_urls['core']])

            os.chdir('core')
            call(['git', 'submodule', 'init'])
            call(['git', 'submodule', 'update'])
            
            os.chdir('3rdparty')
            call(['git', 'checkout', arguments.branch])
            os.chdir('..')

            os.mkdir('data')

            if arguments.level == 'base':
                os.chdir('apps')
                for app_url in chosen_urls['apps']:
                    # repository might not have that specific branch, in that 
                    # case just take master
                    code = call(['git' 'clone ', '-b', arguments.branch, app_url])
                    if code != 0:
                        code = call(['git' 'clone ', '-b', 'master', app_url])

        else:
            print('Can not write to directory %s. Aborted' % directory)
