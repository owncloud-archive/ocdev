"""
Baseclass for creating plugins
"""

class Plugin:


    def __init__(self, *commands):
        self._commands = commands


    def can_handle(self, command):
        if command in self._commands:
            return True
        else:
            return False


    def add_sub_parser(self):
        raise NotImplementedError("Plugin %s does not implement the \
                                   add_sub_parser method" % self._command)


    def run(self):
        raise NotImplementedError("Plugin %s does not implement the run \
                                  method" % self._command)

