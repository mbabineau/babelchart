#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

import babelchart

setup(name = 'babelchart',
      version = babelchart.__version__,
      description = 'Pluggable timeseries data converter',
      long_description='Pluggable timeseries data converter',
      author = 'Mike Babineau',
      author_email = 'michael.babineau@gmail.com',
      # install_requires = [],
      url = 'https://github.com/mbabineau/babelchart',
      packages = ['babelchart'],
      license = 'Apache v2.0',
      platforms = 'Posix; MacOS X; Windows',
      classifiers = [ 'Development Status :: 3 - Alpha',
                      'Intended Audience :: Developers',
                      'Intended Audience :: System Administrators',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Topic :: System :: Logging',
                      ]
      )
