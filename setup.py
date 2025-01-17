#! /usr/bin/env python

from __future__ import with_statement

from setuptools import setup

from fparse import __version__, __doc__

with open('README.rst', 'w') as f:
    f.write(__doc__)

# perform the setup action
setup(
    name="fparse",
    version=__version__,
    description="parse() is the opposite of format()",
    long_description=__doc__,
    author="Richard Jones & Ben Dichter",
    author_email="ben.dichter@catalystneuro.com",
    py_modules=['fparse'],
    url='https://github.com/catalystneuro/fparse',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
    ],
)

# vim: set filetype=python ts=4 sw=4 et si
