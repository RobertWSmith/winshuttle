# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:24:54 2015

@author: A421356
"""

from abc import ABC
import os


class WinshuttleStudio(ABC):
    """\
    Base class for all Winshuttle Studio applications (Transaction & Query)

    Members:
        exe_path string which points to local Winshuttle Studio EXE
        auto_login string which points to local Auto Login File

    Methods:
        subprocess_args returns sequence of arguments suitable for subprocess.Popen
        find_file returns first file path found in sequence
    """

    _exe_path = None
    _auto_login = None

    def __init__(self, exe_path, auto_login):
        """\
        """
        self._exe_path = os.path.normpath(exe_path)
        self.auto_login = auto_login

    @property
    def exe_path(self):
        return self._exe_path

    @property
    def auto_login(self):
        return self._auto_login

    @auto_login.setter
    def auto_login(self, x):
        self._auto_login = x

    def subprocess_args(self, run_script, local_file, **kwargs):
        output = [self.exe_path, run_script, local_file, self.auto_login]
        return output

    @staticmethod
    def find_file(args):
        for arg in args:
            if os.path.isfile(arg):
                return arg


class WinshuttleSortKey(ABC):

    _sort_key = 9999

    def __init__(self, sort_key):
        self.sort_key = sort_key

    @property
    def sort_key(self):
        return self._sort_key

    @sort_key.setter
    def sort_key(self, x):
        if x is None:
            self._sort_key = 9999
        else:
            self._sort_key = int(x)

    def __lt__(self, other):
        return self.sort_key < other.sort_key


class WinshuttleTokenValue(ABC):
    """\
    Winshuttle Token Value base class for subprocess arguments.
    """

    _token = ''
    _value = ''
    _str_fmt = ''
    _sort_key = ''
    _rtv_fmt = ''

    def __init__(self, token, value, **kwargs):
        """\
        Constructor for Token Value object.

        Args:
            token: `str` for the runtime option value, (default '' / empty `str`)
            value: `WinshuttleField` object
            sort_key: `WinshuttleSortKey` or convertible to `WinshuttleSortKey`
        """
        self._token = str(token)
        self._value = value
        self.str_fmt = kwargs.get('str_fmt', '')
        self._sort_key = kwargs.get('sort_key', '')
        self._rtv_fmt = kwargs.get('rtv_fmt', '')

    def __str__(self):
        return self.str_fmt.join([str(self.token), str(self.value)])

    def __lt__(self, other):
        return self.sort_key < other.sort_key

    @property
    def sort_key(self):
        return self._sort_key

    @sort_key.setter
    def sort_key(self, x):
        if isinstance(x, WinshuttleSortKey):
            self._sort_key = x
        else:
            self._sort_key = WinshuttleSortKey(x)

    @property
    def token(self):
        return self._token

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x):
        self._value = x

    @property
    def str_fmt(self):
        return self._str_fmt

    @str_fmt.setter
    def str_fmt(self, x):
        self._str_fmt = x

    @property
    def rtv_fmt(self):
        return self._rtv_fmt

    @rtv_fmt.setter
    def rtv_fmt(self, x):
        self._rtv_fmt = x
