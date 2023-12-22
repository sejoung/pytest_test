"""Module sqltest"""
import logging.config

__version__ = "0.1"

logging.config.fileConfig("../logging.conf")


def print_python_version():
    """Print the Sample version"""
    print(__version__)
