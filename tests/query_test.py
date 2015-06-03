# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 08:41:18 2015

@author: A421356
"""

import unittest

import os

from winshuttle import Query



class Query_Test(unittest.TestCase):

    def setUp(self):
        self.auto_login_token = '-alf'
        self.dummy_alf = 'C:/dummy.alf'
        self.query = Query(self.dummy_alf)

    def tearDown(self):
        pass

    def test_alf(self):
        self.assertNotEqual(str(self.query.auto_login), self.dummy_alf)
        better_alf = ''.join([self.auto_login_token, os.path.normpath(self.dummy_alf)])
        self.assertEqual(str(self.query.auto_login), better_alf)

    def test_exe_path(self):
        self.assertTrue(os.path.isfile(self.query.exe_path))




if __name__ == '__main__':
    unittest.main()
