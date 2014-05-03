"""
Simple class for requiring an argument to match a regex
"""

import re
import argparse


class RegexValidator:

    def __init__(self, regex, errorMsg=None):
        self.regex = re.compile(regex)
        self.errorMsg = errorMsg
        if not self.errorMsg:
            self.errorMsg = "must match regex %s" % regex

    def __call__(self, string):
        match = re.match(self.regex, string)
        if not match:
            raise argparse.ArgumentError(None, self.errorMsg)
        return string