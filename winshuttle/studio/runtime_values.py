# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:56:13 2015

@author: A421356
"""

#from abc import ABC

import collections
import datetime



class QueryRuntimeTableField(object):

    _table = None
    _field = None
    _fmt = '{table}.{field}'

    def __init__(self, table, field):
        self.table = table
        self.field = field

    def __str__(self):
        return str(self.table_field)

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, x):
        self._table = str(x).upper()

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, x):
        self._field = str(x).upper()

    @property
    def table_field(self):
        return self._fmt.format(table=self.table, field=self.field)



class QueryRuntimeValue(object):
    """\
    Query Runtime Values

    Members:
        value required object which will be passed to Winshuttle Query as a Runtime Value filter
        date_fmt static string which converts datetime.date to string
        time_fmt static string which converts datetime.time to string

    Methods:
        value_to_string returns value as a concatenated string
    """

    _value = None
    _multival_join = '|'
    _date_fmt = '%Y%m%d'
    _time_fmt = '%H%M%S'

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value_to_string()

    @property
    def date_fmt(self):
        return self._date_fmt

    @property
    def time_fmt(self):
        return self._time_fmt

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x):
        if isinstance(x, str) or not isinstance(x, collections.Iterable):
            self._value = [x, ]
        else:
            self._value = list([v for v in x])

    def value_to_string(self):
        join_str = ''
        if len(self.value) > 1:
            join_str = self._multival_join
        return join_str.join(self._values_as_string())

    def _values_as_string(self):
        def gen_func(v):
            for v in self.value:
                if isinstance(v, datetime.date):
                    yield v.strftime(self.date_fmt)
                elif isinstance(v, datetime.time):
                    yield v.strftime(self.time_fmt)
                else:
                    yield str(v)
        return list(gen_func(self.value))



class QueryRuntimeVariable(object):
    """\
    Query Runtime Variable object converts stored data to string format for Query object.

    Members:
        table required string which indicates the Query table name
        field required string which indicates the Query field name
        values required object which contains values coercible to string to be used to filter the Query at runtime

    Methods:
        to_string returns string to be passed to subprocess.Popen as part of Query.subprocess_args
    """

    _table = None
    _field = None
    _values = None
    _fmt = '{field}#{values}'

    def __init__(self, table, field, values):
        self.table = table
        self.field = field
        self.values = values

    def __str__(self):
        return str(self.to_string())

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, x):
        self._table = str(x).upper()

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, x):
        self._field = str(x).upper()

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, x):
        self._values = x

    @property
    def query_field(self):
        return QueryRuntimeTableField(self.table, self.field)

    @property
    def values_field(self):
        return QueryRuntimeValue(self.values)

    def to_string(self):
        return self._fmt.format(field=str(self.query_field), values=str(self.values_field))



class QueryRuntimeVariableList(object):
    """\
    Object which converts multiple runtime value filter fields into one string.
    """

    _variables = None
    _arg_join = '~'

    def __init__(self, variable_list):
        self.variables = variable_list

    def __str__(self):
        return str(self.to_string())

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, x):
        self._variables = list([QueryRuntimeVariable(v['table'], v['field'], v['values']) for v in x])

    def to_string(self):
        if len(self.variables) == 1:
            return str(self.variables[0])
        else:
            return self._arg_join.join([str(v) for v in self.variables])



if __name__ == '__main__':
    vals = [{'table': 'VBAK', 'field': 'VBELN', 'values': [1,2,3,4]}, {'table': 'VBAK', 'field': 'AEDAT', 'values': [datetime.date(2014,1,1), datetime.date.today()]}]
    ra = QueryRuntimeVariableList(vals)
    print(str(ra))

