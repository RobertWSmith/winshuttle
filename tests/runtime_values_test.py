# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 08:41:44 2015

@author: A421356
"""

import unittest
import datetime

import winshuttle.studio.runtime_values as rtv

class QueryRuntimeTableField_Test(unittest.TestCase):

    def setUp(self):
        base_test = {'table': 'VBAK', 'field': 'VBELN'}
        self.base_string = '.'.join([base_test.get('table'), base_test.get('field')])
        lowercase_test = {key: value.lower() for key, value in base_test.items()}
        mixed_case = {key: value.capitalize() for key, value in base_test.items()}
        self.test_input_uppercase = base_test
        self.test_input_lowercase = lowercase_test
        self.test_input_mixed_case = mixed_case
        self.test_object_uppercase = rtv.QueryRuntimeTableField(**base_test)
        self.test_object_lowercase = rtv.QueryRuntimeTableField(**lowercase_test)
        self.test_object_mixed_case = rtv.QueryRuntimeTableField(**mixed_case)

    def tearDown(self):
        pass

    def test_table_name(self):
        self.assertEqual(self.test_object_uppercase.table, self.test_input_uppercase.get('table'))
        self.assertNotEqual(self.test_object_lowercase.table, self.test_input_lowercase.get('table'))
        self.assertEqual(self.test_object_lowercase.table, self.test_input_lowercase.get('table').upper())
        self.assertNotEqual(self.test_object_mixed_case.table, self.test_input_mixed_case.get('table'))
        self.assertEqual(self.test_object_mixed_case.table, self.test_input_mixed_case.get('table').upper())

    def test_field_name(self):
        self.assertEqual(self.test_object_uppercase.field, self.test_input_uppercase.get('field'))
        self.assertNotEqual(self.test_object_lowercase.field, self.test_input_lowercase.get('field'))
        self.assertEqual(self.test_object_lowercase.field, self.test_input_lowercase.get('field').upper())
        self.assertNotEqual(self.test_object_mixed_case.field, self.test_input_mixed_case.get('field'))
        self.assertEqual(self.test_object_mixed_case.field, self.test_input_mixed_case.get('field').upper())

    def test_table_field(self):
        self.assertEqual(self.test_object_uppercase.table_field, self.base_string)
        self.assertEqual(self.test_object_lowercase.table_field, self.base_string)
        self.assertEqual(self.test_object_mixed_case.table_field, self.base_string)

    def test_string_representation(self):
        self.assertEqual(str(self.test_object_uppercase), self.base_string)
        self.assertEqual(str(self.test_object_lowercase), self.base_string)
        self.assertEqual(str(self.test_object_mixed_case), self.base_string)


class QueryRutimeValue_Test(unittest.TestCase):

    def setUp(self):
        self.value_separator_string = '|'
        self.date_format_string = '%Y%m%d'
        self.time_format_string = '%H%M%S'
        self.string_test_values = {
            'single': 'ABC',
            'two_values': ['ABC', '123'],
            'sequence': ['1', '2', '3', '4']
            }
        self.number_test_values = {
            'single': 0,
            'two_values': [1, 2],
            'sequence': [1, 2, 3, 4]
        }
        self.date_test_values = {
            'single': datetime.date(2014, 5, 3),
            'two_values': [datetime.date(2014,1,1), datetime.date(2014,12,31)],
            'sequence': [datetime.date(2014,1,1), datetime.date(2014,12,31), datetime.date(2016,1,1)]
        }
        self.time_test_values = {
            'single': datetime.time(0,0,0),
            'two_values': [datetime.time(0,0,0), datetime.time(23,59,59)],
            'sequence': [datetime.time(0,0,1), datetime.time(5,0,15), datetime.time(18,1,1)]
        }

    def tearDown(self):
        pass

    def test_single_string(self):
        test_value = self.string_test_values.get('single')
        t = rtv.QueryRuntimeValue(test_value)
        self.assertEqual(str(t), test_value)

    def test_two_values_string(self):
        test_values = self.string_test_values.get('two_values')
        test_results_string = self.value_separator_string.join(test_values)
        t = rtv.QueryRuntimeValue(test_values)
        self.assertEqual(str(t), test_results_string)

    def test_sequence_string(self):
        test_values = self.string_test_values.get('sequence')
        test_results_string = self.value_separator_string.join(test_values)
        t = rtv.QueryRuntimeValue(test_values)
        self.assertEqual(str(t), test_results_string)

    def test_single_number(self):
        test_value = self.number_test_values.get('single')
        t = rtv.QueryRuntimeValue(test_value)
        self.assertEqual(str(t), str(test_value))

    def test_two_values_number(self):
        test_values = self.number_test_values.get('two_values')
        test_results_string = self.value_separator_string.join([str(v) for v in test_values])
        t = rtv.QueryRuntimeValue(test_values)
        self.assertEqual(str(t), test_results_string)

    def test_sequence_number(self):
        test_values = self.number_test_values.get('sequence')
        test_results_string = self.value_separator_string.join([str(v) for v in test_values])
        t = rtv.QueryRuntimeValue(test_values)
        self.assertEqual(str(t), test_results_string)

    def test_single_date(self):
        test_value = self.date_test_values.get('single')
        t = rtv.QueryRuntimeValue(test_value)
        self.assertEqual(str(t), test_value.strftime(self.date_format_string))

    def test_two_values_date(self):
        test_values = self.date_test_values.get('two_values')
        test_results_string = self.value_separator_string.join([v.strftime(self.date_format_string) for v in test_values])
        t = rtv.QueryRuntimeValue(test_values)
        self.assertEqual(str(t), test_results_string)

    def test_sequence_date(self):
        test_values = self.date_test_values.get('sequence')
        test_results_string = self.value_separator_string.join([v.strftime(self.date_format_string) for v in test_values])
        t = rtv.QueryRuntimeValue(test_values)
        self.assertEqual(str(t), test_results_string)

    def test_single_time(self):
        test_value = self.time_test_values.get('single')
        t = rtv.QueryRuntimeValue(test_value)
        self.assertEqual(str(t), test_value.strftime(self.time_format_string))

    def test_two_values_time(self):
        test_values = self.time_test_values.get('two_values')
        test_results_string = self.value_separator_string.join([v.strftime(self.time_format_string) for v in test_values])
        t = rtv.QueryRuntimeValue(test_values)
        self.assertEqual(str(t), test_results_string)

    def test_sequence_time(self):
        test_values = self.time_test_values.get('sequence')
        test_results_string = self.value_separator_string.join([v.strftime(self.time_format_string) for v in test_values])
        t = rtv.QueryRuntimeValue(test_values)
        self.assertEqual(str(t), test_results_string)


class QueryRuntimeVariable_Test(unittest.TestCase):

    def setUp(self):
        self.table_field_join_string = '.'
        self.table_field_value_join_string = '#'
        self.multivalue_join_string = '|'
        self.single_test_value = {
            'table': 'VBBE',
            'field': 'WERKS',
            'values': 'N636'
        }
        self.two_values_test_value = {
            'table': 'VBBE',
            'field': 'KUNNR',
            'values': ['0000123456', '0000654321']
        }
        self.sequence_test_value = {
            'table': 'VBBE',
            'field': 'MATNR',
            'values': ['000000000000019032', '000000000000163878', '000000000000163890']
        }

    def tearDown(self):
        pass

    def test_single_value(self):
        t = rtv.QueryRuntimeVariable(**self.single_test_value)
        table_field = self.table_field_join_string.join([self.single_test_value.get('table'), self.single_test_value.get('field')])
        test_results_check = self.table_field_value_join_string.join([table_field, self.single_test_value.get('values')])
        self.assertEqual(str(t), test_results_check)

    def test_two_values(self):
        t = rtv.QueryRuntimeVariable(**self.two_values_test_value)
        table_field = self.table_field_join_string.join([self.two_values_test_value.get('table'), self.two_values_test_value.get('field')])
        values_string = self.multivalue_join_string.join(self.two_values_test_value.get('values'))
        test_results_check = self.table_field_value_join_string.join([table_field, values_string])
        self.assertEqual(str(t), test_results_check)

    def test_sequence_of_values(self):
        t = rtv.QueryRuntimeVariable(**self.sequence_test_value)
        table_field = self.table_field_join_string.join([self.sequence_test_value.get('table'), self.sequence_test_value.get('field')])
        values_string = self.multivalue_join_string.join(self.sequence_test_value.get('values'))
        test_results_check = self.table_field_value_join_string.join([table_field, values_string])
        self.assertEqual(str(t), test_results_check)


class QueryRuntimeVariableList_Test(unittest.TestCase):

    def setUp(self):
        self.table_field_join_string = '.'
        self.table_field_value_join_string = '#'
        self.multivalue_join_string = '|'
        self.multiple_runtime_value_join_string = '~'
        self.single_test_value = {
            'table': 'VBBE',
            'field': 'WERKS',
            'values': 'N636'
        }
        self.two_values_test_value = {
            'table': 'VBBE',
            'field': 'KUNNR',
            'values': ['0000123456', '0000654321']
        }
        self.sequence_test_value = {
            'table': 'VBBE',
            'field': 'MATNR',
            'values': ['000000000000019032', '000000000000163878', '000000000000163890']
        }

    def tearDown(self):
        pass

    def test_single_arg(self):
        table_field = self.table_field_join_string.join([self.single_test_value.get('table'), self.single_test_value.get('field')])
        test_results_check = self.table_field_value_join_string.join([table_field, self.single_test_value.get('values')])
        t = rtv.QueryRuntimeVariableList([self.single_test_value])
        self.assertEqual(str(t), test_results_check)

    def test_two_args(self):
        single_table_field = self.table_field_join_string.join([self.single_test_value.get('table'), self.single_test_value.get('field')])
        single_test_results_check = self.table_field_value_join_string.join([single_table_field, self.single_test_value.get('values')])

        two_values_table_field = self.table_field_join_string.join([self.two_values_test_value.get('table'), self.two_values_test_value.get('field')])
        two_values_value_string = self.multivalue_join_string.join(self.two_values_test_value.get('values'))
        two_values_test_results_check = self.table_field_value_join_string.join([two_values_table_field, two_values_value_string])

        test_results_check = self.multiple_runtime_value_join_string.join([single_test_results_check, two_values_test_results_check])
        t = rtv.QueryRuntimeVariableList([self.single_test_value, self.two_values_test_value])
        self.assertEqual(str(t), test_results_check)

    def test_three_args(self):
        single_table_field = self.table_field_join_string.join([self.single_test_value.get('table'), self.single_test_value.get('field')])
        single_test_results_check = self.table_field_value_join_string.join([single_table_field, self.single_test_value.get('values')])

        two_values_table_field = self.table_field_join_string.join([self.two_values_test_value.get('table'), self.two_values_test_value.get('field')])
        two_values_value_string = self.multivalue_join_string.join(self.two_values_test_value.get('values'))
        two_values_test_results_check = self.table_field_value_join_string.join([two_values_table_field, two_values_value_string])

        sequence_values_table_field = self.table_field_join_string.join([self.sequence_test_value.get('table'), self.sequence_test_value.get('field')])
        sequence_values_value_string = self.multivalue_join_string.join(self.sequence_test_value.get('values'))
        sequence_values_test_results_check = self.table_field_value_join_string.join([sequence_values_table_field, sequence_values_value_string])

        test_results_check = self.multiple_runtime_value_join_string.join([single_test_results_check, two_values_test_results_check, sequence_values_test_results_check])
        t = rtv.QueryRuntimeVariableList([self.single_test_value, self.two_values_test_value, self.sequence_test_value])
        self.assertEqual(str(t), test_results_check)



if __name__ == '__main__':
    unittest.main()



