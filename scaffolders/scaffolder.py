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
import datetime

from jinja2 import Environment, FileSystemLoader


class Scaffolder:

    def __init__(self, cmd, scaffolderDirectory):
        self._cmd = cmd
        self._scaffolderDirectory = scaffolderDirectory

    
    def canHandle(self, args):
        if args.which == self._cmd:
            return True
        else:
            return False

    def _bindCustomContext(self, params):
        params['now'] = datetime.datetime.utcnow()
        return params
        

    def build(self, templateDirectory, outDirectory, params={}):
        params = self._bindCustomContext(params)

        env = Environment(loader=FileSystemLoader(templateDirectory))

        # loop through all files in the templates folder and write them compiled
        # to the current directory
        scaffoldDirectory = os.path.join(templateDirectory, self._scaffolderDirectory)

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

                rendered = env.get_template(relativeTemplatePath).render(params)

                with open(outPath, 'w+') as target:
                    target.write(rendered)
