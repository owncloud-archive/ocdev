from ocdev.plugins.startapp.startapp import StartApp
from ocdev.plugins.setup.setup import SetUp
from ocdev.plugins.ci.ci import ContinousIntegration
from ocdev.plugins.version.version import Version

PLUGINS = [SetUp(), StartApp(), ContinousIntegration(), Version()]