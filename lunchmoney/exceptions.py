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


class LunchMoneyImportError(LunchMoneyError, ImportError):
    """
    Lunch Money Import Error
    """
