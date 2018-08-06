# -*- coding: utf-8 -*-

import unittest
from robot import Robot


class RobotTestCase(unittest.TestCase):

    def test_instance(self):
        robot = Robot()
        self.assertIsInstance(robot, Robot)

    def test_instance_properties(self):
        robot = Robot()
        self.assertEqual(robot.X, -1)
        self.assertEqual(robot.Y, -1)
        self.assertEqual(robot.Dir, '')

    def test_update_within_bounds(self):
        robot = Robot()
        robot.update(0, 1, 'NORTH')
        self.assertEqual(robot.X, 0)
        self.assertEqual(robot.Y, 1)
        self.assertEqual(robot.Dir, 'NORTH')

    def test_update_out_of_bounds(self):
        robot = Robot()
        robot.update(10, 10, 'SOUTH')
        self.assertEqual(robot.X, -1)
        self.assertEqual(robot.Y, -1)
        self.assertEqual(robot.Dir, '')

    def test_update_invalid_direction(self):
        robot = Robot()
        robot.update(2, 1, 'BLA')
        self.assertEqual(robot.X, -1)
        self.assertEqual(robot.Y, -1)
        self.assertEqual(robot.Dir, '')

    def test_str(self):
        robot = Robot()
        self.assertEqual(robot.__str__(), 'Uninitialised')
        robot.update(1, 2, 'EAST')
        self.assertEqual(robot.__str__(), '1,2,EAST')

    def test_static_get_next_prev_direction(self):
        self.assertIsNone(Robot.get_next_prev_direction('BLA', 1))
        self.assertEqual(Robot.get_next_prev_direction('NORTH', 0), 'NORTH')
        self.assertEqual(Robot.get_next_prev_direction('NORTH', 1), 'EAST')
        self.assertEqual(Robot.get_next_prev_direction('WEST', 1), 'NORTH')
        self.assertEqual(Robot.get_next_prev_direction('NORTH', -1), 'WEST')
        self.assertEqual(Robot.get_next_prev_direction('WEST', -1), 'SOUTH')
