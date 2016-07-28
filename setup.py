#!/usr/bin/env python

from distutils.core import setup


setup(
    name='librfdevice',
    author='Ian S. Cohee',
    version='0.1',
    package=['librfdevice'],
    package_dir={'librfdevice': 'src/librfdevice'},
    description='A Python module that defines various radio components for use with RFcat.',
)
