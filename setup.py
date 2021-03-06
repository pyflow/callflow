#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import platform

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    path = os.path.join(package, "__init__.py")
    init_py = open(path, "r", encoding="utf8").read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_long_description():
    """
    Return the README.
    """
    return open("README.md", "r", encoding="utf8").read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]

requirements = [
    "websockets==8.*",
    "httptools==0.1.*",
    "uvloop>=0.14.0",
    "basepy>=0.3.1",
    "setproctitle"
]


setup(
    name="callflow_core",
    version=get_version("callflow"),
    url="https://github.com/zeaphoo/callflow",
    license="MIT",
    description="multi protocol, auto-cluster server framework.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Wei Zhuo",
    author_email="zeaphoo@qq.com",
    packages=get_packages("callflow"),
    install_requires=requirements,
    data_files=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython"
    ],
    entry_points={
        'console_scripts': ['callflow-manager=callflow.manager:run_manager']
    }
)
