#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="psg",
    version="0.0.4",
    keywords=["pakistan", "bills", "sui", "gas", "query", "search"],

    description="Pakistan SUI gas bills and tariff.",
    long_description=open('README.md').read(),

    project_urls={
        'Homepage': 'https://www.techtum.dev/work-psg-220228.html#work-psg-220228',
        'Source': 'https://github.com/siphr/psg',
        'Tracker': 'https://github.com/siphr/psg/issues',
    },

    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['psg'],
    platforms="any",
)
