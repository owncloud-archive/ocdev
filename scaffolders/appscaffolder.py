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

from jinja2 import Template


class AppFrameworkScaffolder:

    def __init__(self):
        self._templateDirectory = 'appframework/app/' # must end with /


    def addParserTo(self, mainParser):
        parser = mainParser.add_parser('createapp', help='Create an app')
        parser.set_defaults(which='createapp')

        parser.add_argument(
            '--type',
            help='Decides which template folder should be taken in the templates folder',
            default='appframework'
        )
        parser.add_argument(
            '--license',
            help='The used license',
            default='agpl3'
        )
        parser.add_argument(
            'app_name',
            help='Name of the app in lower case seperate with underscores'
        )


    def canHandle(self, args):
        if args.which == 'createapp':
            return True
        else:
            return False


    def scaffold(self, args, currentDirectory, templatesDirectory):
        authors = []
        moreAuthors = True
        while moreAuthors:
            authors.append({
                'name': input('Please enter the author of the app: '),
                'email': input('Please enter teh author\'s e-mail: ')
            })
            moreAuthors = input('Do you wish to add another author? [y/N]') == 'y'

        # loop through all files in the templates folder and write them compiled
        # to the current directory
        appFolder = os.path.join(currentDirectory, args.app_name)
        os.mkdir(appFolder)

        scaffoldDirectory = os.path.join(templatesDirectory, self._templateDirectory)
        for root, dirs, files in os.walk(scaffoldDirectory):
            
            # first create all the directories on that level
            for folder in dirs:
                absPath = os.path.join(root, folder)
                createPath = self._getAppDirectory(absPath, scaffoldDirectory, appFolder)
                os.mkdir(createPath)

            # then read the templates and create the parsed files
            for template in files:
                absPath = os.path.join(root, template)
                createPath = self._getAppDirectory(absPath, scaffoldDirectory, appFolder)

                with open(absPath, 'r') as f:
                    content = f.read()
                    tpl = Template(content)
                    rendered = tpl.render({
                        'authors': authors,
                        'appName': self._getAppNameDict(args)
                    })

                    with open(createPath, 'w+') as target:
                        target.write(rendered)


    def _getAppNameDict(self, args):
        name = args.app_name

        words = name.split('_')
        map(lambda word: word.title(), words) # uppercase first letter of all words

        return {
            'id': name,
            'full': ' '.join(words),
            'namespace': ''.join(words)
        }


    def _getAppDirectory(self, path, templatesDirectory, appFolder):
        relativePath = path.replace(templatesDirectory, '', 1)
        return os.path.join(appFolder, relativePath)
