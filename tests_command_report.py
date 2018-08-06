# -*- coding: utf-8 -*-

import unittest
from command_report import ReportCommand


class ReportCommandTestCase(unittest.TestCase):
    """
    There are little to no tests here since the REPORT command basically only prints out the robot's current position.
    It doesn't do any manipualtions and does not return anything.
    I have "written" these tests BEFORE the command's implementation but due to the fact that the command basically
    does nothing and I have boiletplate code for it from other commands, the tests pass even though the command
    has not yet been implemented. I am committing code following the TDD practice but in this specific case it won't
    make a difference.
    """

    def test_instance(self):
        rep = ReportCommand()
        self.assertIsInstance(rep, ReportCommand)

    def test_run_missing_arguments(self):
        with self.assertRaises(Exception):
            ReportCommand().run()
