#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-forum',
    version="0.1",
    author='Pardus ANKA',
    author_email='pisiciftligi@pardus-linux.org',
    description='Pardus ANKA Forum',
    url='http://pardus-anka.org',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
