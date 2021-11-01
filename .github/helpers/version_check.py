#!/usr/bin/env python3

"""
Compare two Versions Using SemVer comparison
Make sure the `CURRENT_VERSION` and `MAIN_VERSION` environment variables are set
"""

from os import environ
from sys import argv

# noinspection PyPackageRequirements
from packaging.version import Version

try:
    try:
        current_version = argv[1]
    except IndexError:
        current_version = Version(environ["CURRENT_VERSION"])
    try:
        main_version = argv[2]
    except IndexError:
        main_version = Version(environ["MAIN_VERSION"])
    assert current_version >= main_version
except KeyError:
    raise EnvironmentError(f"You must set the `CURRENT_VERSION` and `MAIN_VERSION` "
                           "environment variables or pass them in as arguments, "
                           "respectively.")
except AssertionError:
    raise ValueError(f"Your current version ({current_version}) is not greater than "
                     f"the `main` branch ({main_version})")
