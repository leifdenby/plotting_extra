import os
import re
import sys
import sysconfig
import platform
import subprocess

from distutils.version import LooseVersion
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def run_tests(self):
        import shlex
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(['tests/'])
        sys.exit(errno)

setup(
    name='plotting_extra',
    version='0.0.1',
    author='Leif Denby',
    author_email='l.c.denby@leeds.ac.uk',
    description='Utilities for making special plots',
    long_description='',
    # add custom build_ext command
    cmdclass=dict(test=PyTest),
    zip_safe=False,
    tests_require=['pytest'],
    # install_requires=['attrdict',],
    packages=["plotting_extra",],
)
