# -*- coding: utf-8 -*-

from command import CommandBase
from parser import CommandsParser
from robot import UNINITIALIZED as RobotUninitialisedState
import logging


logger = logging.getLogger(__name__)


class MoveCommand(CommandBase):
    """
    Implementation of the MOVE command
    """
    def __init__(self):
        self.ID = 'MOVE'

    def run(self, robot, arguments=None):
        """
        Execute the logic of the MOVE command
        """
        if robot is None:
            return

        # NOTE: This has to be done for every command except PLACE. I Could have also implemented this completely in
        # the Robot class. The choice between these two options, in my opinion, is a design decision for who's
        # responsible - is the Robot responsible for all it's business rules (and so there's not really a need for
        # Commands - they can be implemented inside the Robot, or is he a dumb state machine and the rules are applied
        # by the commands. I believe in the context of this exercise both are valid, and so I chose the latter.
        # Also, please note that the Initialised/PLACED rule IS DIFFERENT from the bounds rule. I consider the latter
        # to be input validation and not really a business rule (but of course, the line is very thin here).
        if str(robot) == RobotUninitialisedState:
            return

        logger.info('Running command MOVE {}'.format(robot.Dir))
        if robot.Dir == 'NORTH':
            robot.update(robot.X, robot.Y+1, robot.Dir)
        elif robot.Dir == 'SOUTH':
            robot.update(robot.X, robot.Y-1, robot.Dir)
        elif robot.Dir == 'EAST':
            robot.update(robot.X+1, robot.Y, robot.Dir)
        elif robot.Dir == 'WEST':
            robot.update(robot.X-1, robot.Y, robot.Dir)


# Register with the CommandParser class so that this command can be used by the parser
CommandsParser.Register(MoveCommand())
