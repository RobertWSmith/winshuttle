# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:04:19 2015

@author: A421356
"""

import setuptools as st
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

st.setup(
    name = "winshuttle",
    version = "0.0.4",
    packages = st.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "*.egg-info"]),
    author = "Robert Smith",
    author_email = "rob_smith@goodyear.com",
    description = "utilities for calling Winshuttle scripts via the subprocess module",
#    install_requires = [],
    test_suite = 'tests'
)
