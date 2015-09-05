# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:30:43 2015

@author: A421356
"""

from winshuttle.base import WinshuttleTokenValue
from winshuttle.studio.runtime_values import QueryRuntimeVariableList

import os
#import urllib.parse as urlp
import collections

#WinshuttleRuntimeTuple = collections.namedtuple('WinshuttleRuntimeTuple', field_names = ['table', 'field', 'values'])


class StringTokenValue(WinshuttleTokenValue):

    pass


class URLPathTokenValue(WinshuttleTokenValue):

    pass


class LocalPathTokenValue(WinshuttleTokenValue):

    def __init__(self, token, value):
        super().__init__(token=token, value=os.path.normpath(value))


class RuntimeTokenValue(WinshuttleTokenValue):
    """\
    Runtime Value List holder (Query Only)
    """
    def __init__(self, value, **kwargs):
        kwargs['rtv_fmt'] = '~'
        super().__init__('-rtv', QueryRuntimeVariableList(value), **kwargs)

    def __str__(self):
        if isinstance(self.value, collections.Iterable) and not isinstance(self.value, str):
            my_val = self.rtv_fmt.join(list([str(v) for v in self.value]))
        else:
            my_val = str(self.value)
        return self.str_fmt.join([str(self.token), my_val])

    @property
    def value(self):
        return super().value

    @value.setter
    def value(self, x):
        super().value = QueryRuntimeVariableList(x)


if __name__ == '__main__':
    import datetime
    import winshuttle

    vals = [{'table': 'VBAK', 'field': 'VBELN', 'values': [1,2,3,4]}, {'table': 'VBAK', 'field': 'AEDAT', 'values': [datetime.date(2014,1,1), datetime.date.today()]}]
    ra = RuntimeTokenValue(vals)
    print(str(ra))

    winshuttle.base.WinshuttleTokenValue('-rtv', vals)

