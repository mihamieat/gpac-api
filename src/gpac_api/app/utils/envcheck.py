# -*- coding: utf-8 -*-
"""environment checker modules."""
import os


def is_testing_env():
    """Check if the application is running in a testing environment.

    This function determines whether the application is in a testing mode by checking the
    environment variable "TESTING". It returns True if the variable is set to a truthy value,
    indicating that the application should behave as if it is in a testing environment.

    Returns:
        bool: True if the application is in a testing environment, False otherwise.
    """
    return os.environ.get("TESTING") is not None and os.environ.get(
        "TESTING"
    ).lower() in ("true", "1", "yes")
