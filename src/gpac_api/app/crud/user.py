# -*- coding: utf-8 -*-
"""handle CRUD operations for user model. """

from fastapi.security import HTTPBasicCredentials

from src.gpac_api.app.db.database import db
from src.gpac_api.app.schemas.user import UserResponseSchema


def find_user(credentials: HTTPBasicCredentials) -> UserResponseSchema:
    """
    Retrieve a user from the database based on provided credentials.

    Args:
        credentials (HTTPBasicCredentials): The HTTP basic credentials\
 containing the username to search for.

    Returns:
        UserResponseSchema: The user document if found, otherwise None.
    """
    collection = db.user
    return collection.find_one({"username": credentials.username})
