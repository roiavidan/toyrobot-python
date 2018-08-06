# -*- coding: utf-8 -*-

from command import CommandBase
from parser import CommandsParser
import logging


logger = logging.getLogger(__name__)


class PlaceCommand(CommandBase):
    """
    Implementation of the PLACE command
    """
    def __init__(self):
        self.ID = 'PLACE'

    def run(self, robot, arguments):
        """
        Execute the logic of the PLACE command
        """
        if robot is None:
            return

        if isinstance(arguments, str):
            arguments = [x.strip() for x in arguments.split(',') if x.strip() != '']

        logger.info('Running command PLACE with arguments {},{},{}'.format(arguments[0], arguments[1], arguments[2]))
        robot.update(int(arguments[0]), int(arguments[1]), arguments[2])


# Register with the CommandParser class so that this command can be used by the parser
CommandsParser.Register(PlaceCommand())
