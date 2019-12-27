#!/usr/bin/env python3

from setuptools import setup
from distutils.util import convert_path

main_ns = {}
vpath = convert_path('photorename/version.py')
with open(vpath) as vfile:
    exec(vfile.read(), main_ns)

setup(
    name='photorename',
    version=main_ns['__version__'],
    description='bulk rename photos in a dictionary',
    author='Robert Lehmann',
    author_email='lehmrob@posteo.net',
    url='https://github.com/lehmrob',
    packages=['photorename'],
    entry_points = {
        'console_scripts': ['phore=photorename.cli:main'],
    },
    install_requires=[
        'exif',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
