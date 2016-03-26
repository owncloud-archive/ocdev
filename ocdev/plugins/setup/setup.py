import os
import stat
from subprocess import check_call, CalledProcessError

from ocdev.plugins.setup.dependencyerror import DependencyError
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

        parser.add_argument('--type', help='If SSH or HTTPS should be used to '
                            'fetch the sources. Defaults to HTTPS since you '
                            'need push access in order to use SSH',
                            choices=['https', 'ssh'])
        parser.add_argument('--branch', help='The branch which should be '
                            'checked out, defaults to master', default='master')
        parser.add_argument('--dir', help='The directory name, defaults to '
                            'core', default='core')
        parser.add_argument('--no-history', help='Clones with git depth 1 and '
                            'therefore is very fast but ommits history. This is '
                            'great for continuous integration builds '
                            'but should be avoided when developing normally',
                            action='store_true')
        parser.add_argument('level', help='core, base or a specific repository '
                            'in ownCloud organization on GitHub. core only sets '
                            'up a working core setup, base also installs apps '
                            'like news, notes, calendar, gallery, music, '
                            'documents and contacts. To clone a specific '
                            'repository, you can type the repository name in '
                            'lowercase, e.g. ocdev setup music.',
                            default='core')

    def run(self, arguments, directory, settings):
        """
        throws a DependencyError if git is not installed
        """
        directory = os.path.normpath(directory)
        try:
            self.setup(arguments, directory, settings)
        except FileNotFoundError as e:
            print(e)
            raise DependencyError('Failed to clone repository because Git '
                                  'is not installed')


    def setup(self, arguments, directory, settings):
        level = arguments.level
        branch = arguments.branch
        target_dir = arguments.dir
        if arguments.type:
            type = arguments.type
        else:
            type = settings.get_value('setup', 'type')

        no_history = arguments.no_history

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
                'repo': 'git@github.com:owncloud/%s.git' % level,
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
                'repo': 'https://github.com/owncloud/%s.git' % level,
            }
        }[type]

        # check if directory is writeable
        if os.access(directory, os.W_OK):
            if (arguments.level == 'core' or arguments.level == 'base'):
                self.clone_fallback(urls['core'], branch, target_dir, no_history)

                os.chdir(arguments.dir)

                os.chdir('3rdparty')
                check_call(['git', 'checkout', arguments.branch])
                os.chdir('..')

            if arguments.level == 'base':
                os.chdir('apps')
                for app_url in urls['apps']:
                    self.clone_fallback(app_url, branch, None, no_history)
            elif arguments.level != 'core':
                print(
                    '\nSelected setup type is neither core nor base. Trying '
                    'to clone repository named %s\n' % level
                )

                self.clone_fallback(urls['repo'], branch, None, no_history)

            if arguments.level == 'base' or arguments.level == 'core':
                print(
                    '\nSuccessfully set up development environment!\n\n'
                    'Setup ownCloud by changing into the cloned directory and '
                    'run\n\n    ocdev server\n\n'
                    'and setup your installation at http://localhost:8080\n\n'
                )
        else:
            print('Can not write to directory %s. Aborted' % directory)


    def clone_fallback(self, url, branch=None, directory=None, no_history=False):
        """
        Clone branch and fall back to master if there is no branch
        """
        try:
            return self.clone_repo(url, branch, directory, no_history)
        except CalledProcessError as e:
            return self.clone_repo(url, 'master', directory, no_history)


    def clone_repo(self, url, branch='master', directory=None, no_history=False):
        """
        Clones a branch
        """
        cmd = ['git', 'clone', '--recursive']

        if branch:
            cmd = cmd + ['-b', branch]
        if no_history:
            cmd = cmd + ['--depth', '1']

        cmd.append(url);

        if directory:
            cmd.append(directory)


        return check_call(cmd)
