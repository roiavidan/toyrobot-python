# -*- coding: utf-8 -*-

import unittest
from mock import patch
from main import load_command_list, read_commands_from_console


class MainTestCase(unittest.TestCase):

    def test_no_args(self):
        self.assertEqual(load_command_list(), [])

    def test_args_valid_file_name(self):
        import tempfile
        with tempfile.NamedTemporaryFile() as tf:
            self.assertEqual(load_command_list(tf.name), [])

    def test_load_from_non_empty_file(self):
        import tempfile
        with tempfile.NamedTemporaryFile() as tf:
            tf.write("MOVE\nREPORT")
            tf.flush()
            self.assertEqual(load_command_list(tf.name), ['MOVE', 'REPORT'])

    def test_args_non_existant_file(self):
        import tempfile, time
        with self.assertRaises(Exception):
            load_command_list('{}/{}'.format(tempfile.gettempdir(), int(time.time())))

    def test_read_commands_from_console(self):
        with patch('__builtin__.raw_input', side_effect=['PLACE 0,0,NORTH', 'move', 'REPORT', '']):
            commands = read_commands_from_console()
            self.assertItemsEqual(['PLACE 0,0,NORTH', 'MOVE', 'REPORT'], commands)
