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
import os.path
from sys import exit
import re

from owncloud_scaffolding.scaffolders.scaffolder import Scaffolder, RegexValidator


class ResourceScaffolder(Scaffolder):

    def __init__(self):
        super().__init__('resource')


    def addParserTo(self, mainParser):
        parser = mainParser.add_parser('resource', help='Create a resource')
        parser.set_defaults(which='resource')
        parser.add_argument(
            'name',
            help='Name of the resource',
            type=RegexValidator('^[a-zA-Z_]+$')
        )


    def scaffold(self, args, templateDirectory, currentDirectory):
        # get directory 
        try:
            directory = self.findAppDirectory(currentDirectory)
        except OSError:
            print('Error: App directory not found!')
            exit(1)


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
            'resource': {
                'name': args.name
            }
        }


        # build controller
        self.buildFile(
            templateDirectory,
            'appframework/resource/controller.php',
            os.path.join(directory, 'controller/%scontroller.php' % args.name),
            params
        )

        # build testcase
        self.buildFile(
            templateDirectory,
            'appframework/resource/controllertest.php',
            os.path.join(directory, 'tests/unit/controller/%sControllerTest.php' % args.name.title()),
            params
        )

        self.buildFile(
            templateDirectory,
            'appframework/resource/service.php',
            os.path.join(directory, 'service/%sservice.php' % args.name),
            params
        )

        self.buildFile(
            templateDirectory,
            'appframework/resource/servicetest.php',
            os.path.join(directory, 'tests/unit/service/%sServiceTest.php' % args.name.title()),
            params
        )

        self.buildFile(
            templateDirectory,
            'appframework/resource/mapper.php',
            os.path.join(directory, 'db/%smapper.php' % args.name),
            params
        )

        self.buildFile(
            templateDirectory,
            'appframework/resource/mappertest.php',
            os.path.join(directory, 'tests/unit/db/%sMapperTest.php' % args.name.title()),
            params
        )

        self.buildFile(
            templateDirectory,
            'appframework/resource/entity.php',
            os.path.join(directory, 'db/%s.php' % args.name),
            params
        )

        self.appendFile(
            templateDirectory,
            'appframework/resource/routes.php',
            os.path.join(directory, 'appinfo/routes.php'),
            params
        )

        self.appendFile(
            templateDirectory,
            'appframework/resource/diconfig.php',
            os.path.join(directory, 'dependencyinjection/diconfig.php'),
            params
        )
