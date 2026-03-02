"""Configure a custom logger"""

"""
Logging levels
DEBUG: Detailed information useful when debugging
INFO: COnfirmation things are working as intended
WARNING: An indication something unexpected happened or might happen
ERROR: More serious problem
CRITICAL: problem that crashes the program
"""

import logging

def setup_logger(name):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.WARNING)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s  | %(message)s',
            datefmt = '%H:%M:%S'
            )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger