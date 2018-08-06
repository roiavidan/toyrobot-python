# -*- coding: utf-8 -*-

import copy
import logging


logger = logging.getLogger(__name__)


class CommandsParser(object):
    """
    Responsible for returning the next command, while one exist.
    Also controls the business rule which defines the order of acceptable commands.
    """

    # Known command objects
    COMMANDS = {}

    def __init__(self, commands=None):
        self.cmd_list = copy.copy(commands) if commands is not None else []

    def get_next_command(self):
        """
        This is the main logic for the command parser. It will iterate over the commands list and if a valid command
        is found, instantiate an object for it and return it with it's arguments.
        If an invalid one is found, it will be skipped.
        Retuns None when reaching the list' end.
        """
        command = None
        while len(self.cmd_list):
            temp = self.cmd_list.pop(0).strip() + ' '
            cmd, args = temp.split(' ', 1)
            if cmd in CommandsParser.COMMANDS:
                command = (CommandsParser.COMMANDS[cmd], args)
                break
            else:
                logger.info('Unknown command "{}"'.format(cmd))

        logger.info('get_next_command() returning {}'.format(command))
        return command

    @staticmethod
    def Register(command):
        """
        Register the given command object with the parser, so it can be used when needed.
        """
        CommandsParser.COMMANDS[command.ID] = command
        logger.info('Registering new command instance for "{}"'.format(command.ID))
