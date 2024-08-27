# -*- coding: utf-8 -*-
"""security package."""

import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()


class CurrentUser:
    """
    Class to manage the current user's authentication state.

    Attributes:
        granted (bool): Indicates whether access has been granted to the user.
    """

    def __init__(self):
        """
        Initialize a new instance with default settings.

        Args:
            None

        Returns:
            None
        """
        self.granted = False

    def verify_credentials(
        self,
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    ):
        """
        Verify the provided HTTP basic credentials for access.


        Args:
            credentials: The HTTP basic credentials containing the username and password.

        Returns:
            bool: True if the credentials are valid and access is granted.

        Raises:
            HTTPException: If the username or password is incorrect: 401.
        """
        is_correct_username = self.compare_strings(credentials.username, "eteph")
        is_correct_password = self.compare_strings(credentials.password, "$wordfi$h")
        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        self.granted = True
        return self.granted

    def compare_strings(self, current_str, correct_str):
        """
        Compare two strings for equality in a secure manner.

        Args:
            current_str (str): The string to compare against the correct string.
            correct_str (str): The correct string to compare with.

        Returns:
            bool: True if the strings are equal, False otherwise.
        """
        current_str_bytes = current_str.encode("utf8")
        correct_str_bytes = correct_str.encode("utf8")
        return secrets.compare_digest(current_str_bytes, correct_str_bytes)
