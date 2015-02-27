from ocdev.plugins.startapp.startapp import StartApp
from ocdev.plugins.setup.setup import SetUp
from ocdev.plugins.ci.ci import ContinousIntegration
from ocdev.plugins.appstore.appstore import AppStore
from ocdev.plugins.server.server import Server

PLUGINS = [SetUp(), StartApp(), ContinousIntegration(), Server()] # AppStore()
