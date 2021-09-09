#!/usr/bin/env python3

# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunchmoney Exceptions
"""

from requests.exceptions import HTTPError


class LunchMoneyError(Exception):
    """
    Base Exception for Lunch Money
    """


class EnvironmentVariableError(LunchMoneyError, EnvironmentError):
    """
    Lunch Money Missing Environment Variable Error
    """


class LunchMoneyHTTPError(LunchMoneyError, HTTPError):
    """
    Lunch Money HTTP Error
    """
