# -*- coding: utf-8 -*-
import os
import unittest


def testsuite():
    """Automatically discover all tests in this folder."""
    return unittest.TestLoader().discover(os.path.dirname(__file__))
