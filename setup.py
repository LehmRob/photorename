#!/usr/bin/env python3

from setuptools import setup

setup(
    name='photorename',
    version='1.0.0',
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
