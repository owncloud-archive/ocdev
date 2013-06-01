#!/usr/bin/env python3
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


import argparse
import os
from sys import exit
from os.path import dirname, join, realpath

from owncloud_scaffolding import TEMPLATE_DIRECTORY
from owncloud_scaffolding.scaffolders.appscaffolder import AppScaffolder
from owncloud_scaffolding.scaffolders.resourcescaffolder import ResourceScaffolder


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--templates', help='Path to the template directory',
        default=TEMPLATE_DIRECTORY)
    parsers = parser.add_subparsers(help='sub-command help')

    # list active scaffolders
    scaffolders = [
        AppScaffolder(),
        ResourceScaffolder()
    ]

    for scaffolder in scaffolders:
        scaffolder.addParserTo(parsers)

    args = parser.parse_args()

    # make sure there's an argument
    try:
        args.which
    except AttributeError:
        print("Missing arguments\nType owncloud.py --help for usage.")
        exit(1)

    # get the scaffolder which can handle the input
    for scaffolder in scaffolders:
        if scaffolder.canHandle(args):
            scaffolder.scaffold(args, args.templates, os.getcwd())


if __name__ == '__main__':
    main()
