# -*- coding: utf-8 -*-

import logging


logger = logging.getLogger(__name__)

UNINITIALIZED = 'Uninitialised'


class Robot(object):
    """
    This is the implementation of the Robot, which knows it' position and direction.
    """

    # "private" property for defining bounds and valid values
    TABLE = {
        'X': 5,
        'Y': 5,
        'DIRECTIONS': ['NORTH', 'EAST', 'SOUTH', 'WEST']
    }

    def __init__(self):
        self.X = -1
        self.Y = -1
        self.Dir = ''

    def __str__(self):
        """
        Returns a string representation of the Robot's current state and position.
        """
        if self.X == -1 or self.Y == -1 or self.Dir == '':
            logger.info('Robot is uninitialised')
            return UNINITIALIZED

        return '{},{},{}'.format(self.X, self.Y, self.Dir)

    def update(self, x, y, dir):
        """
        Update the robot's current position and direction, if valid and within the acceptable bounds.
        """
        if x >= 0 and x < Robot.TABLE['X'] and y >= 0 and y < Robot.TABLE['Y'] and dir in Robot.TABLE['DIRECTIONS']:
            self.X = x
            self.Y = y
            self.Dir = dir
            logger.info('Updated Robot to ({})'.format(self))
        else:
            logger.info('Unable to update Robot\'s position due to invalid input {},{},{}'.format(x, y, dir))

    @staticmethod
    def get_next_prev_direction(current, next_or_prev):
        """
        This helper method is used to determine the next direction a Robot faces.
        It calculates it by looking at the current one and going in circles on position to the left or to the right.
        next_or_prev receives either a positive value (right), a negative value (left) or zero (same direction).
        This method could have been an instance method, removing the need for the current direction argument, but I
        chose to leave it as a static since:
        1. It uses a "static private" property for the class - TABLE['DIRECTIONS'] - I can maintain the property hidden
           for everything outside of the class, encapsulating all related logic here
        2. In the future I might want to calculate something like this outside the context of a Robot
        """
        try:
            cur = Robot.TABLE['DIRECTIONS'].index(current)
        except ValueError:
            logger.info('Unknown direction "{}"'.format(current))
            return None

        if next_or_prev == 0:
            return current

        # transform into -1 or 1
        next_or_prev = next_or_prev / abs(next_or_prev)
        # use modulus to calculate next step inside a circle
        new_dir_index = (cur + next_or_prev) % len(Robot.TABLE['DIRECTIONS'])
        # return new direction
        logger.debug('{} direction for {} is {}'.format(next_or_prev, current, Robot.TABLE['DIRECTIONS'][new_dir_index]))
        return Robot.TABLE['DIRECTIONS'][new_dir_index]
