# -*- coding: utf-8 -*-
"""
============================
crossplatformshell
============================
"""
from __future__ import (print_function, division, absolute_import,
                       unicode_literals)

import pathlib
import io
import os
import shutil
import distutils.dir_util

# Use subprocess32 if available
try:
    import subprocess32 as subprocess
except:
    import subprocess as subprocess

# Versioneer versioning
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def new_path(path_string):
    """Return pathlib.Path, expanding '~' to a user's HOME directory"""
    return pathlib.Path(os.path.expanduser(path_string))


def copy(src_path, dst_path):
    shutil.copy(str(src_path), str(dst_path))

cp = copy


def copy_tree(src_path, dst_path):
    """Recursively copy all files and folders from src_path to dst_path"""
    distutils.dir_util.copy_tree(str(src_path), str(dst_path))

cp_r = copy_tree

def mkdir(path):
    """Make a directory from the specified path"""
    os.mkdir(str(path))


def remove(path):
    """Remove the specified path."""
    os.remove(str(path))

def rm(*args):
    for path in args:
        try:
            os.remove(str(path))
        except OSError:
            pass

def rmtree(path):
    """Recursively remove paths."""
    shutil.rmtree(str(path))

def rm_rf(path):
    """Recursively delete directories, if they exist"""
    try:
        shutil.rmtree(str(path))
    except OSError:
        pass

def read_file(filename):
    return io.open(str(filename)).read()


def write_file(filename, string, encoding="utf-8"):
    io.open(str(filename), 'w', encoding=encoding).write(string)


