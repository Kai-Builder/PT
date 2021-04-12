import os

import sys


# Command Line.  . .
def parse(string: str, split_):
    return string.split(split_)


def args(string: str, regex):
    arr = string.split(regex)
    arr.pop(0)
    return arr


def command(string: str, regex):
    arr = string.split(regex)

    return arr.pop(0)


