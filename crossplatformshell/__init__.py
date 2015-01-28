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
import platform

# Use subprocess32 if available
try:
    import subprocess32 as subprocess
except:
    import subprocess as subprocess

windows = platform.system() == 'Windows'

git = 'git.cmd' if windows else 'git'

# Versioneer versioning
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def check_output(*args, **kwargs):
    """Check_output, but prints and  Use printing=False to turn """
    printing = kwargs.pop('printing', True)

    try:
        out_lines = subprocess.check_output(*args, **kwargs).decode('utf-8').splitlines()
    except subprocess.CalledProcessError as e:
        # Wrap in try/except so that check_output can print
        raise e

    if printing:
        for line in out_lines:
            print(line)

    return out_lines


def new_path(path_string):
    """Return pathlib.Path, expanding '~' to a user's HOME directory"""
    return pathlib.Path(os.path.expanduser(path_string))


def mkdir(*args):
    """Make a directory from the specified path"""
    for arg in args:
        os.mkdir(str(arg))


def remove(path):
    """Remove the specified path."""
    os.remove(str(path))


def rmtree(path):
    """Recursively remove paths."""
    shutil.rmtree(str(path))


def copy(src_path, dst_path):
    shutil.copy(str(src_path), str(dst_path))

cp = copy


def copy_tree(src_path, dst_path):
    """Recursively copy all files and folders from src_path to dst_path"""
    distutils.dir_util.copy_tree(str(src_path), str(dst_path))

cp_r = copy_tree


def rm(*args):
    for path in args:
        try:
            os.remove(str(path))
        except OSError:
            pass


def rm_rf(*args):
    """Recursively delete directories, if they exist"""
    for path in args:
        try:
            os.remove(str(path))
        except OSError:
            pass


def read_file(filename, encoding="utf-8"):
    with io.open(str(filename), encoding=encoding) as f:
        text = f.read()
    return text


def write_file(filename, string, encoding="utf-8"):
    with io.open(str(filename), 'w', encoding=encoding) as f:
        f.write(string)
