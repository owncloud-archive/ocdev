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
import sys
import re

from owncloud_scaffolding.scaffolders.scaffolder import Scaffolder


class ControllerScaffolder(Scaffolder):

    def __init__(self):
        super().__init__('controller')


    def addParserTo(self, mainParser):
        parser = mainParser.add_parser('controller', help='Create a controller')
        parser.set_defaults(which='controller')
        parser.add_argument(
            '--license',
            help='The used license',
            default='AGPLv3'
        )
        parser.add_argument(
            '--headers',
            help='If license headers should be included in every file',
            default=True
        )
        parser.add_argument(
            'controllerName',
            help='Name of the controller in CamelCase'
        )
        parser.add_argument(
            'controllerMethodName',
            help='Name of the controller method in pascalCase'
        )



    def scaffold(self, args, templateDirectory, currentDirectory):
        # get directory 
        try:
            directory = self.findAppDirectory(currentDirectory)
        except OSError:
            print('Error: App directory not found!')
            sys.exit(1)


        appName = os.path.basename(os.path.dirname(directory))

        # get authors from authors file
        authors = []
        with open(os.path.join(directory, 'AUTHORS'), 'r') as f:
            regex = re.compile('(.+) <(.+)>')
            for line in f:
                search = re.search(regex, line)
                if search:
                    authors.append({
                        'name': search.group(1),
                        'email': search.group(2)
                    })

        # build the namespace and name from the app id
        words = appName.split('_')
        upperCaseWords = map(lambda word: word.title(), words)
        fullName = ' '.join(upperCaseWords)
        namespace = fullName.replace(' ', '')

        params = {
            'app': {
                'id': appName,
                'authors': authors,
                'fullName': fullName,
                'namespace': namespace,
                'license': {
                    'type': args.license,
                    'headers': args.headers
                }
            },
            'controller': {
                'name': args.controllerName,
                'methodName': args.controllerMethodName
            }
        }


        # build controller
        self.buildFile(
            templateDirectory,
            'appframework/controller/controller.php',
            os.path.join(directory, 'controller/%s.php' % args.controllerName.lower()),
            params
        )

        # build testcase
        self.buildFile(
            templateDirectory,
            'appframework/controller/test.php',
            os.path.join(directory, 'tests/unit/controller/%sTest.php' % args.controllerName),
            params
        )




