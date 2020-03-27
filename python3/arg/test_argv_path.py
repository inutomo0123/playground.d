#!/usr/bin/env python3

from unittest import TestCase
import subprocess as sp
from sys import argv

class TestArgvPath(TestCase):

    def test_none(self):

        cmd='./argv_path.py'
        output = sp.check_output(cmd.split()).decode('UTF-8')

        self.assertEqual('False\n', output, \
                         'コマンドライン引数がないとき')

    def test_not_file(self):
        cmd='./argv_path.py XYZ'
        output = sp.check_output(cmd.split()).decode('UTF-8')

        self.assertEqual('False\n', output,
                         'コマンドライン引数がパスじゃない')

    def test_file_path(self):
        cmd='./argv_path.py /dev/null'
        output = sp.check_output(cmd.split()).decode('UTF-8')

        self.assertEqual('True\n', output,
                         'コマンドライン引数がパスのとき')
