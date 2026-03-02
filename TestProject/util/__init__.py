"""Utils package - provides helper methods and logging configuration"""

#grab specific functions from specific files
from .helpers import format_name, truncate
from .validators import is_valid_age, is_valid_email
from .logger import setup_logger

#what functions are imported when someone uses * in import statement
__all__ = ["is_valid_email"]