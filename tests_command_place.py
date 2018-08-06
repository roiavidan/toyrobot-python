# -*- coding: utf-8 -*-

import unittest
from command_place import PlaceCommand

"""
NOTE: This line and the tests below are not aligned with the strict definition of unit testing since the
inclusion of another class here, which might be modified in the future actually generates a dependency between
the two and thus makes it more of an integration test than a unit one.
However, I have chosen to do so anyway for two reasons:
1. For the sake of simplicity in this excercise. A better approach should use an Interface or a Mock.
2. The command itself (and all of them actually) is highly dependant (and coupled) with the Robot class, so
   keeping them apart makes little sense.
It is important to remember that if a test fails here, the developer should be aware that the failure might be
due to changes in the Robot class and not only in the command class. One more step of investigation should be
applied.
"""
from robot import Robot


class PlaceCommandTestCase(unittest.TestCase):

    def test_instance(self):
        place = PlaceCommand()
        self.assertIsInstance(place, PlaceCommand)

    def test_run_valid(self):
        robot = Robot()
        place = PlaceCommand()
        place.run(robot, '3,4,WEST')
        self.assertEqual(robot.X, 3)
        self.assertEqual(robot.Y, 4)
        self.assertEqual(robot.Dir, 'WEST')

    def test_run_invalid(self):
        robot = Robot()
        place = PlaceCommand()
        place.run(robot, '3,4,BOO')
        self.assertNotEqual(robot.X, 3)
        self.assertNotEqual(robot.Y, 4)
        self.assertNotEqual(robot.Dir, 'BOO')

    def test_run_invalid_arguments(self):
        robot = Robot()
        place = PlaceCommand()
        with self.assertRaises(ValueError):
            place.run(robot, 'A,B,C')

    def test_run_missing_arguments(self):
        with self.assertRaises(Exception):
            PlaceCommand().run()
        with self.assertRaises(Exception):
            PlaceCommand().run(Robot())
