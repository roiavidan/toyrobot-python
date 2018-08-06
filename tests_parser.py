# -*- coding: utf-8 -*-

import unittest
from parser import CommandsParser


class ParserTestCase(unittest.TestCase):

    class MockCommand(object):

        def __init__(self, id):
            self.ID = id


    def test_instance(self):
        parser = CommandsParser()
        self.assertIsInstance(parser, CommandsParser)

    def test_get_next_on_none_list(self):
        parser = CommandsParser()
        self.assertIsNone(parser.get_next_command()) # None

    def test_get_next_on_empty_list(self):
        parser = CommandsParser([])
        self.assertIsNone(parser.get_next_command()) # None

    def test_get_next_on_non_empty_list(self):
        CommandsParser.Register(ParserTestCase.MockCommand('MOVE'))
        CommandsParser.Register(ParserTestCase.MockCommand('REPORT'))
        parser = CommandsParser(['MOVE', 'REPORT'])
        self.assertIsNotNone(parser.get_next_command())
        self.assertIsNotNone(parser.get_next_command())
        self.assertIsNone(parser.get_next_command()) # MOVE, REPORT, None
        CommandsParser.COMMANDS = {}

    def test_get_next_with_invalid_command(self):
        CommandsParser.Register(ParserTestCase.MockCommand('MOVE'))
        parser = CommandsParser(['MOVE', 'DANCE', 'SIT', 'MOVE'])
        self.assertIsNotNone(parser.get_next_command())
        self.assertIsNotNone(parser.get_next_command())
        self.assertIsNone(parser.get_next_command()) # MOVE, MOVE, None
        CommandsParser.COMMANDS = {}

    def test_get_next_with_last_invalid_command(self):
        CommandsParser.Register(ParserTestCase.MockCommand('MOVE'))
        parser = CommandsParser(['MOVE', 'DANCE', 'SIT'])
        self.assertIsNotNone(parser.get_next_command())
        self.assertIsNone(parser.get_next_command()) # MOVE, None
        CommandsParser.COMMANDS = {}

    def test_static_register_method(self):
        self.assertEquals(len(CommandsParser.COMMANDS), 0)
        mock = ParserTestCase.MockCommand('mock')
        CommandsParser.Register(mock)
        self.assertEquals(len(CommandsParser.COMMANDS), 1)
        self.assertIsInstance(CommandsParser.COMMANDS['mock'], ParserTestCase.MockCommand)
