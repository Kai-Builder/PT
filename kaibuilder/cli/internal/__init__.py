import os

import kaibuilder.servermanager as sm

import importlib as importlib


def parg(a):
    return sm.args(a, ' ')


def pcmd(a):
    return sm.command(a, ' ')

def dynamic_import(module):
    return importlib.import_module(module)

def full(a):
    return sm.parse(a, ' ')



class CommandLineInterface:

    def begin(self):
        while True:
            i = input(os.getcwd() + "\S>")
            command = sm.command(i, ' ')
            args = sm.args(i, ' ')
            try:
                bstrrap = dynamic_import("kaibuilder.cmd." + command)
                bstrrap.main(args)
            except Exception:
                print("Unknown Command")