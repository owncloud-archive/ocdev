#!/usr/bin/env python3
"""
ownCloud developer tool which can be used to create ownCloud apps
"""

__author__ = 'Bernhard Posselt'
__copyright__ = 'Copyright 2012-2014, Bernhard Posselt'
__license__ = 'AGPL3+'
__maintainer__ = 'Bernhard Posselt'
__email__ = 'dev@bernhard-posselt.com'

# parse version from version.txt file
from ocdev.version import get_version
__version__ = get_version()

import argparse
import sys
import os

from ocdev.plugins import PLUGINS
from ocdev.plugins.pluginerror import PluginError
from ocdev.config import UserSettings

def main():
    # read file in home directory
    user_config_path = os.path.join(os.path.expanduser('~'), '.ocdevrc')
    settings = UserSettings(user_config_path)
    settings.read()

    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=__version__,
                        help='Print out the ocdev version')
    parsers = parser.add_subparsers(help='commands')

    for plugin in PLUGINS:
        plugin.add_sub_parser(parsers)

    arguments = parser.parse_args()

    # get he plugin that can handle the input
    if not hasattr(arguments, 'which'):
        parser.print_help();
        exit(1)
    try:
        for plugin in PLUGINS:
            if plugin.can_handle(arguments.which):
                plugin.run(arguments, os.getcwd(), settings)

    except PluginError as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    main()
