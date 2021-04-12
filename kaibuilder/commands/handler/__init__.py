import os

import importlib as ip

class CommandLineCommand(object):
    def __init__(self, name):
        self.name = name

    def load(self):
        return ip.import_module(self.name)

    def download(self, module):
        return ip.import_module(module)
