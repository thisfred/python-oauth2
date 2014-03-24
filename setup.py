#!/usr/bin/env python
from setuptools import setup, find_packages

PKG = 'oauth2'

setup(name=PKG,
      version='1.5.212-trapit',
      description="library for OAuth version 1.0",
      author="Joe Stump",
      author_email="joe@simplegeo.com",
      url="http://github.com/simplegeo/python-oauth2",
      packages=find_packages(),
      install_requires=['httplib2'],
      license="MIT License",
      keywords="oauth",
      zip_safe=True,
      test_suite="tests",
      tests_require=['coverage', 'mock'])
