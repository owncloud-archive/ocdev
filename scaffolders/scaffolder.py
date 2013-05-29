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

class Scaffolder:

    def __init__(self, cmd, templateDirectory):
        self._cmd = cmd
        self._templateDirectory = templateDirectory
    

    def canHandle(self, args):
        if args.which == self._cmd:
            return True
        else:
            return False


    def build(self, inDirectory, outDirectory, params={}):
        # loop through all files in the templates folder and write them compiled
        # to the current directory
        scaffoldDirectory = os.path.join(inDirectory, self._templateDirectory)

        for root, dirs, files in os.walk(scaffoldDirectory):
            
            # first create all the directories on that level
            for folder in dirs:
                absPath = os.path.join(root, folder)
                createPath = self._getAppDirectory(absPath, scaffoldDirectory, outDirectory)
                os.mkdir(createPath)

            # then read the templates and create the parsed files
            for template in files:
                absPath = os.path.join(root, template)
                createPath = self._getAppDirectory(absPath, scaffoldDirectory, outDirectory)

                with open(absPath, 'r') as f:
                    content = f.read()
                    tpl = Template(content)
                    rendered = tpl.render(params)

                    with open(createPath, 'w+') as target:
                        target.write(rendered)


    def _getAppDirectory(self, path, templatesDirectory, appFolder):
        relativePath = path.replace(templatesDirectory, '', 1)
        return os.path.join(appFolder, relativePath)

