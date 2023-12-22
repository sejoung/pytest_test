"""Module providing a function printing Sample version."""
import logging.config

from .core import hmm
from .gonaver import fetch_naver_comic

__version__ = "0.1"

logging.config.fileConfig("../logging.conf")


def print_python_version():
    """Print the Sample version"""
    print(__version__)
