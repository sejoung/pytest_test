"""Module core function"""

import logging

from . import helpers

logger = logging.getLogger("root")


def __get_hmm():
    logger.info("""Get a thought.""")
    return "hmmm..."


def hmm():
    """로그 정보"""
    logger.info("""Contemplation...""")
    if helpers.get_answer():
        result = __get_hmm()
        logger.info(result)
        return result
    return None
