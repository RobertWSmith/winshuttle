# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 08:41:36 2015

@author: A421356
"""

import unittest

import os

import winshuttle.studio.token as tkn

class StringTokenValue_Test(unittest.TestCase):

    def setUp(self):
        self.simple_test_case = {'token': 'abc', 'value': '123'}

    def tearDown(self):
        pass

    def test_simple_case(self):
        test_obj = tkn.StringTokenValue(**self.simple_test_case)
        expected_results = ''.join([self.simple_test_case.get('token'), self.simple_test_case.get('value')])
        self.assertEqual(str(test_obj), expected_results)


class URLPathTokenValue_Test(unittest.TestCase):

    def setUp(self):
        self.simple_test_case = {'token': 'abc', 'value': 'http://www.google.com'}

    def tearDown(self):
        pass

    def test_simple_case(self):
        test_obj = tkn.URLPathTokenValue(**self.simple_test_case)
        expected_results = ''.join([self.simple_test_case.get('token'), self.simple_test_case.get('value')])
        self.assertEqual(str(test_obj), expected_results)


class LocalPathTokenValue_Test(unittest.TestCase):

    def setUp(self):
        self.simple_test_case = {'token': 'abc', 'value': 'C:/abc.txt'}

    def tearDown(self):
        pass

    def test_simple_case(self):
        test_obj = tkn.LocalPathTokenValue(**self.simple_test_case)
        base_results = ''.join([self.simple_test_case.get('token'), self.simple_test_case.get('value')])
        expected_results = ''.join([self.simple_test_case.get('token'), os.path.normpath(self.simple_test_case.get('value'))])
        self.assertNotEqual(str(test_obj), base_results)
        self.assertEqual(str(test_obj), expected_results)


class RuntimeTokenValue_Test(unittest.TestCase):

    def setUp(self):
        self.rtv_string = '-rtv'
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
        test_results_check = ''.join([self.rtv_string, test_results_check])
        t = tkn.RuntimeTokenValue([self.single_test_value])
        self.assertEqual(str(t), test_results_check)

    def test_two_args(self):
        single_table_field = self.table_field_join_string.join([self.single_test_value.get('table'), self.single_test_value.get('field')])
        single_test_results_check = self.table_field_value_join_string.join([single_table_field, self.single_test_value.get('values')])

        two_values_table_field = self.table_field_join_string.join([self.two_values_test_value.get('table'), self.two_values_test_value.get('field')])
        two_values_value_string = self.multivalue_join_string.join(self.two_values_test_value.get('values'))
        two_values_test_results_check = self.table_field_value_join_string.join([two_values_table_field, two_values_value_string])

        test_results_check = self.multiple_runtime_value_join_string.join([single_test_results_check, two_values_test_results_check])
        test_results_check = ''.join([self.rtv_string, test_results_check])
        t = tkn.RuntimeTokenValue([self.single_test_value, self.two_values_test_value])
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
        test_results_check = ''.join([self.rtv_string, test_results_check])
        t = tkn.RuntimeTokenValue([self.single_test_value, self.two_values_test_value, self.sequence_test_value])
        self.assertEqual(str(t), test_results_check)





if __name__ == '__main__':
    unittest.main()
