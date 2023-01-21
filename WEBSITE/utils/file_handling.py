# file_handling.py
import os
from config import ALLOWED_EXTENSIONS


def file_is_allowed(filename) -> bool:
    """
    This function checks if the specified file is allowed.
    Allowed extensions are specified via ALLOWED_EXTENSIONS in config.py.

    Parameter:
    - filename (str): The name of the file

    Returns:
    bool: True if file is allowed; otherwise false
    """
    _, file_extension = os.path.splitext(filename)
    if not file_extension:
        return False
    return file_extension in ALLOWED_EXTENSIONS
