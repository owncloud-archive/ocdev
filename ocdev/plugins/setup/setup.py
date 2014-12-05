import os
import stat
from subprocess import check_call

from ocdev.plugins.errors import DependencyError
from ocdev.plugins.plugin import Plugin


class Arguments:

    def __init__(self, level='core', branch='master', type='https',
                      directory='core'):
        self.level = level
        self.branch = branch
        self.type = type
        self.dir = directory


class SetUp(Plugin):

    def __init__(self):
        super().__init__('setup')


    def add_sub_parser(self, main_parser):
        parser = main_parser.add_parser('setup', help='Setup')
        parser.set_defaults(which='setup')

        parser.add_argument('--type', help='If SSH or HTTPS should be used to \
                            fetch the sources. Defaults to HTTPS since you need \
                            push access in order to use SSH', default='https',
                            choices=['https', 'ssh'])
        parser.add_argument('--branch', help='The branch which should be \
                            checked out, defaults to master', default='master')
        parser.add_argument('--dir', help='The directory name, defaults to core',
                            default='core')
        parser.add_argument('level', help='core, base or a specific repository \
                            in ownCloud organization on GitHub. core only sets up \
                            a working core setup, base also installs apps like \
                            news, notes, calendar, gallery, music, documents \
                            and contacts. To clone a specific repository, you \
                            can type the repository name in lowercase, e.g. \
                            ocdev setup music.',
                            default='core')

    def run(self, arguments, directory, settings):
        """
        throws a DependencyError if git is not installed
        """
        directory = os.path.normpath(directory)
        try:
            self.git_clone(arguments, directory)
        except FileNotFoundError as e:
            raise DependencyError('Failed to clone repository because Git ' +
                                  'is not installed')


    def git_clone(self, arguments, directory):
        urls = {
            'ssh': {
                'core': 'git@github.com:owncloud/core.git',
                'apps': [
                    'git@github.com:owncloud/news.git',
                    'git@github.com:owncloud/activity.git',
                    'git@github.com:owncloud/gallery.git',
                    'git@github.com:owncloud/music.git',
                    'git@github.com:owncloud/notes.git',
                    'git@github.com:owncloud/calendar.git',
                    'git@github.com:owncloud/contacts.git',
                    'git@github.com:owncloud/documents.git',
                    'git@github.com:owncloud/chat.git',
                    'git@github.com:owncloud/bookmarks.git'
                ],
                arguments.level: 'git@github.com:owncloud/' + arguments.level + '.git',
            },
            'https': {
                'core': 'https://github.com/owncloud/core.git',
                'apps': [
                    'https://github.com/owncloud/news.git',
                    'https://github.com/owncloud/activity.git',
                    'https://github.com/owncloud/gallery.git',
                    'https://github.com/owncloud/music.git',
                    'https://github.com/owncloud/notes.git',
                    'https://github.com/owncloud/calendar.git',
                    'https://github.com/owncloud/contacts.git',
                    'https://github.com/owncloud/documents.git',
                    'https://github.com/owncloud/chat.git',
                    'https://github.com/owncloud/bookmarks.git'
                ],
                arguments.level: 'https://github.com/owncloud/' + arguments.level + '.git',
            }
        }

        chosen_urls = urls[arguments.type]

        # check if directory is writeable
        if os.access(directory, os.W_OK):
            if (arguments.level == 'core' or arguments.level == 'base'):
                code = check_call(['git', 'clone', '--recursive', '-b',
                        arguments.branch, chosen_urls['core'], arguments.dir])
                if code != 0:  # default to master if branch fails
                    check_call(['git', 'clone', '--recursive', '-b', 'master',
                        chosen_urls['core'], arguments.dir])

                os.chdir(arguments.dir)

                os.chdir('3rdparty')
                check_call(['git', 'checkout', arguments.branch])
                os.chdir('..')

            if arguments.level == 'base':
                os.chdir('apps')
                for app_url in chosen_urls['apps']:
                    # repository might not have that specific branch, in that
                    # case just take master
                    code = check_call(['git', 'clone', '-b', arguments.branch, app_url])
                    if code != 0:
                        code = check_call(['git', 'clone', '-b', 'master', app_url])
            elif arguments.level != 'core':
                print('\nSelected setup type is neither core nor base. Trying to')
                print('clone repository named ' + arguments.level + '.')
                # repository might not have that specific branch, in that
                # case just take master
                code = check_call(['git', 'clone', '-b', arguments.branch, chosen_urls[arguments.level]])
                if code != 0:
                    code = check_call(['git', 'clone', '-b', 'master', chosen_urls[arguments.level]])

            if arguments.level == 'base' or arguments.level == 'core':
                print('\nSuccessfully set up development environment!\n\n')
                print('Setup ownCloud by changing into the cloned directory and run\n')
                print('    php -S localhost:8080\n')
                print('and setup your isntallation at http://localhost:8080\n\n')
        else:
            print('Can not write to directory %s. Aborted' % directory)
