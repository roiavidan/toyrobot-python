# -*- coding: utf-8 -*-

import argparse
import logging
from parser import CommandsParser
from robot import Robot

# Load all known commands
# NOTE: in a real-world scenario, we will probably have some code to discover and load commands (as modules)
# automatically but in the current case, I believe it is enough to load them "hard-coded"
import command_place, command_move, command_left, command_right, command_report

# Logging is important. It was not a part of the required scope for this exercise, but I decided to add it anyway as a
# good practice. As such, we will write/append a log to a file here, but in real world scenario, it'll probably be
# configured to use Syslog or some similar facility.
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='/tmp/robot.log')


def load_command_list(filename=None):
    """
    Return parsed array of commands from given file or an empty array if no file given.
    Raises an exception if a file is given but is not readable.
    """
    contents = None
    if filename:
        logger.debug('Attempting to read commands from "{}"'.format(filename))
        with open(filename, 'r') as fp:
            contents = fp.read().strip()

    if not contents:
        contents = ''

    # Split data as lines (ignore empty)
    return [l.strip().upper() for l in contents.split('\n') if l.strip() != '']


def read_commands_from_console():
    """
    Provides a simple way to read the list of commands from the console.
    """
    cmds = []
    print 'Please provide commands for REA Robot. One command per line. An empty line finishes the input:'
    while True:
        line = raw_input()
        if line:
            cmds += [line.upper()]
        else:
            break

    return cmds


def main():
    """
    Main logic loop.
    Not tested under Unit testing, since it's more suitable for integration tests!
    """
    parser = argparse.ArgumentParser(description='REA Robot')
    parser.add_argument('--c', metavar='FILE', type=str, required=False, help='File with commands to execute. One command per line')
    args = parser.parse_args()

    # Get list of commands to execute
    commands = load_command_list(args.c)
    if len(commands) == 0:
        commands = read_commands_from_console()

    logger.debug('List of commands to execute: {}'.format(commands))

    # Run the Robot
    robot = Robot()
    cmd_parser = CommandsParser(commands)
    while True:
        cmd_and_args = cmd_parser.get_next_command()
        if cmd_and_args:
            cmd_and_args[0].run(robot, cmd_and_args[1])
        else:
            break


if __name__ == '__main__':
    main()
