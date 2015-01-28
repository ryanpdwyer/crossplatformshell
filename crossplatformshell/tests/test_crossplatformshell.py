# -*- coding: utf-8 -*-
"""
Tests for `crossplatformshell` module.
"""
from __future__ import (print_function, division, absolute_import,
                       unicode_literals)

import unittest
import os
import tempfile


from crossplatformshell import (new_path, copy, copy_tree, mkdir, remove,
                                rmtree, write_file, windows, git, check_output,
                                subprocess)


class TestCheckOutput(unittest.TestCase):

    def test_output_raises_error(self):
        self.assertRaises(subprocess.CalledProcessError,
                          check_output, [git, 'notagitcommand'])

    def test_output_git_version(self):
        out = check_output([git, '--version'])[0]
        self.assertTrue('git version' in out)


class TestCrossplatformshell(unittest.TestCase):

    fname = 'tempfile.txt'

    def setUp(self):
        self.dir = new_path(tempfile.mkdtemp())
        self.file = self.dir/self.fname
        write_file(self.file, "Test file contents\n")

    def test_copy(self):
        copied_file = 'tempfile_copy.txt'
        copy(self.file, self.dir/copied_file)
        self.assertTrue(os.path.isfile(str(self.dir/copied_file)))

    def test_mkdir(self):
        new_dir = 'new_dir'
        mkdir(self.dir/new_dir)
        self.assertTrue((self.dir/new_dir).is_dir())

    def test_copy_tree(self):
        new_dir = 'new_dir'
        cp_dir = 'copied_dir'
        new_file = 'testfile.txt'
        mkdir(self.dir/new_dir)
        write_file(self.dir/new_dir/new_file, "Test file contents\n")
        copy_tree(self.dir/new_dir, self.dir/cp_dir)
        self.assertTrue((self.dir/new_dir).is_dir())
        self.assertTrue((self.dir/new_dir/new_file).is_file())

    def tearDown(self):
        rmtree(self.dir)
