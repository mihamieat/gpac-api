# -*- coding: utf-8 -*-
"""security package."""

import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.gpac_api.app.crud.user import find_user

security = HTTPBasic()


# pylint: disable=R0903
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
        user_data = find_user(credentials)
        if not user_data or not secrets.compare_digest(
            credentials.password, user_data["password"]
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        self.granted = True
        return self.granted
