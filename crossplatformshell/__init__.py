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


def check_output(*args, **kwargs):
    """Subprocess check_output, but prints commands and output by default.
    Also allows printing of error message for helpful debugging.

    Use print_all=False to turn off all printing."""
    print_all = kwargs.pop('print_all', None)
    if print_all is not None:
        print_in = print_all
        print_out = print_all
    else:
        print_in = kwargs.pop('print_in', True)
        print_out = kwargs.pop('print_out', True)

    if print_in:
        print('')
        print(' '.join(args[0]))

    try:
        out_bytes = subprocess.check_output(*args, **kwargs)
        out_lines = out_bytes.decode('utf-8').splitlines()
    except subprocess.CalledProcessError as e:
        # Wrap in try/except so that check_output can print
        raise e

    if print_out:
        for line in out_lines:
            print(line)

    return out_lines


windows = platform.system() == 'Windows'


def find_git_cmd(windows):
    git = 'git'

    if windows:
        try:
            check_output([git, '--version'])
        except subprocess.CalledProcessError:
            try:
                git = 'git.cmd'
                check_output([git, '--version'])
            except subprocess.CalledProcessError:
                msg = "git does not appear to be on your path."
                raise subprocess.CalledProcessError(msg)

    return git

git = find_git_cmd(windows)


def new_path(path_string):
    """Return pathlib.Path, expanding '~' to a user's HOME directory"""
    return pathlib.Path(os.path.expanduser(path_string))


def mkdir(*args):
    """Make directories for the specified paths."""
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
    """Delete files, if they exist.
    Fail silently if a file doesn't exist."""
    for path in args:
        try:
            os.remove(str(path))
        except OSError:
            pass


def rm_rf(*args):
    """Recursively delete directories, if they exist."""
    for path in args:
        try:
            shutil.rmtree(str(path))
        except OSError:
            pass


def read_file(filename, encoding="utf-8"):
    with io.open(str(filename), encoding=encoding) as f:
        text = f.read()
    return text


def write_file(filename, string, encoding="utf-8"):
    with io.open(str(filename), 'w', encoding=encoding) as f:
        f.write(string)


# Versioneer versioning
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
