# -*- coding: utf-8 -*-


class CommandBase(object):
    """
    We don't have Interfaces (not abstract classes) in Python, but this pattern can be used anyway.
    This class exists as a base abstract class (=interface) for all implemented commands.
    I won't be writing unit tests for this one since I consider it irrelevant for Interfaces.
    """

    def __init__(self):
        raise NotImplemented()

    def run(self, robot, arguments=None):
        raise NotImplemented()
