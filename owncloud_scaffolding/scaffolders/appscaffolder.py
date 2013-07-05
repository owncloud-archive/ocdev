"""
ownCloud scaffolder tool

Copyright (C) 2013 Bernhard Posselt, <nukewhale@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import os

from owncloud_scaffolding.scaffolders.scaffolder import Scaffolder, RegexValidator


class AppScaffolder(Scaffolder):

    def __init__(self):
        super().__init__('startapp', [
            '*vendor*',
            '*3rdparty*'
        ])

        self._scaffoldingDirectories = {
            'appframework': 'appframework/app/',
            'classic': 'app/app/'
        }


    def addParserTo(self, mainParser):
        parser = mainParser.add_parser('startapp', help='Create an app')
        parser.set_defaults(which='startapp')

        parser.add_argument(
            '--type',
            help='Decides which template folder should be taken in the templates folder',
            default='appframework',
            type=RegexValidator('^[a-z_]+$')
        )
        parser.add_argument(
            'app_name',
            help='Name of the app in lower case seperate with underscores',
            type=RegexValidator('^[a-z_]+$')
        )


    def scaffold(self, args, templateDirectory, outDirectory):
        authors = []
        moreAuthors = True
        while moreAuthors:
            authors.append({
                'name': self.ask('Please enter the author of the app: ', '.+',
                    'Please enter a name'),
                'email': self.ask('Please enter the author\'s e-mail: ', '.+',
                    'Please enter a mail address')
            })
            moreAuthors = self.ask('Do you wish to add another author? [y/N]: ') == 'y'

        description = self.ask('Please enter a short description of the app: ')

        # build the namespace and name from the app id
        words = args.app_name.split('_')
        upperCaseWords = map(lambda word: word.title(), words)
        fullName = ' '.join(upperCaseWords)
        namespace = fullName.replace(' ', '')
        appName = namespace.lower()

        params = {
            'app': {
                'id': appName,
                'authors': authors,
                'fullName': fullName,
                'namespace': namespace,
                'license': {
                    'type': args.license,
                    'headers': args.headers
                },
                'description': description
            }
        }

        appFolder = os.path.join(outDirectory, appName)

        try:
            os.mkdir(appFolder)
        except FileExistsError:
            print("Error:", appFolder, "already exists!")
            exit(1)
        self.buildDirectory(
            templateDirectory,
            self._scaffoldingDirectories[args.type],
            appFolder,
            params
        )





