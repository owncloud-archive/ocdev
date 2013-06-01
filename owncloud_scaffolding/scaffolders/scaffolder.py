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
import re
from argparse import ArgumentError
from datetime import datetime
from fnmatch import fnmatch

from jinja2 import Environment, FileSystemLoader


class RegexValidator:

    def __init__(self, regex, errorMsg=None):
        self.regex = re.compile(regex)
        self.errorMsg = errorMsg
        if not self.errorMsg:
            self.errorMsg = "must match regex %s" % regex

    def __call__(self, string):
        match = re.match(self.regex, string)
        if not match:
            raise ArgumentError(None, self.errorMsg)
        return string


class Scaffolder:

    def __init__(self, cmd, ignoredPatterns=[]):
        self._cmd = cmd
        self._ignoredPatterns = ignoredPatterns


    def canHandle(self, args):
        if args.which == self._cmd:
            return True
        else:
            return False

    def ask(self, question, validate='.*', errorMsg=''):
        regex = re.compile(validate)
        result = input(question)
        if not re.match(regex, result):
            print(errorMsg)
            self.ask(question, validate, errorMsg)
        else:
            return result


    def _bindCustomContext(self, params):
        params['now'] = datetime.utcnow()
        return params


    def buildDirectory(self, templateDirectory, scaffolderDirectory, outDirectory, params={}):
        params = self._bindCustomContext(params)

        env = Environment(loader=FileSystemLoader(templateDirectory))

        # loop through all files in the templates folder and write them compiled
        # to the current directory
        scaffoldDirectory = os.path.join(templateDirectory, scaffolderDirectory)

        for root, dirs, files in os.walk(scaffoldDirectory):

            # first create all the directories on that level
            for folder in dirs:
                # construct the paths for reading and writing
                absPath = os.path.join(root, folder)
                relativeScaffoldPath = absPath.replace(scaffoldDirectory, '', 1)
                outPath = os.path.join(outDirectory, relativeScaffoldPath)
                os.mkdir(outPath)

            # then read the templates and create the parsed files
            for template in files:
                # construct the paths for reading and writing
                absPath = os.path.join(root, template)
                relativeTemplatePath = absPath.replace(templateDirectory, '', 1)
                relativeScaffoldPath = absPath.replace(scaffoldDirectory, '', 1)
                outPath = os.path.join(outDirectory, relativeScaffoldPath)

                ignore = False
                for pattern in self._ignoredPatterns:
                    if fnmatch(relativeScaffoldPath, pattern):
                        ignore = True

                if ignore:
                    with open(absPath, 'r') as f:
                        rendered = f.read()
                else:
                    rendered = env.get_template(relativeTemplatePath).render(params)

                with open(outPath, 'w+') as target:
                    target.write(rendered)


    def buildFile(self, templateDirectory, fileIn, fileOut, params={}):
        params = self._bindCustomContext(params)
        env = Environment(loader=FileSystemLoader(templateDirectory))

        rendered = env.get_template(fileIn).render(params)

        with open(fileOut, 'w+') as target:
            target.write(rendered)


    def appendFile(self, templateDirectory, fileIn, fileOut, params={}):
        params = self._bindCustomContext(params)
        env = Environment(loader=FileSystemLoader(templateDirectory))

        rendered = env.get_template(fileIn).render(params)

        with open(fileOut, 'a') as target:
            target.write(rendered)


    def findAppDirectory(self, currentPath):
        regex = re.compile('(.+)appinfo/info.xml')
        appDirectory = None
        for root, dirs, files in os.walk(currentPath):
            for file in files:
                absPath = os.path.join(root, file)
                search = re.search(regex, absPath)
                if search:
                    return search.group(1)

        # go up one directory if the directory was not found
        folderHigher = os.path.realpath(os.path.join(currentPath, '..'))
        if os.path.exists(folderHigher) and folderHigher != '/':
            return self.findAppDirectory(folderHigher)
        else:
            raise OSError()
