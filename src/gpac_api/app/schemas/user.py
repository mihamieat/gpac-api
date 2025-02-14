# -*- coding: utf-8 -*-
"""user models."""

from bson import ObjectId
from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    """
    UserResponseSchema represents a user in the application with essential attributes.

    Attributes:
        username (str): The unique identifier for the user.
        password (str): The user's password for authentication.
        email (str): The user's email address for communication.
        description (str): A brief description of the user.

    """

    _id: ObjectId
    username: str
    password: str
    email: str
    description: str

    # pylint: disable=R0903
    class Config:
        """
        Configuration settings for the notification schema.

        Attributes:
            json_encoders (dict).
        """

        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
