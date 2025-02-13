# -*- coding: utf-8 -*-
"""Notif schemas."""

from typing import List, Literal, Optional
from bson import ObjectId
from pydantic import BaseModel


class NotifCreateSchema(BaseModel):
    """
    Notif Create Schema

    Attributes:
        recipients (List[str]): A list of email addresses.
        gpus (List[str]): A list of GPU identifiers.
        mail_content (str): The content of the mails.
        message_type (Literal["warning", "info", "error"]):.
    """

    recipients: List[str]
    gpus: List[str]
    mail_content: Optional[str]
    message_type: Literal["warning", "info", "error"] = (
        "info"  # Optional with a default value
    )


class NotifResponseSchema(BaseModel):
    """
    Notif Respons Schema

    Attributes:
        id (str): The unique identifier .
        recipients (List[str]): A list of email addresses.
        gpus (List[str]): A list of GPU identifiers .
        mail_content (str): The content of the mail.
        message_type (Literal["warning", "info", "error"]).

        Config:
            allow_population_by_field_name (bool): Enables population of \
fields by their names.
            json_encoders (dict): Custom encoders for specific types, such \
as converting ObjectId to string.
    """

    _id: str
    recipients: List[str]
    gpus: List[str]
    mail_content: str
    message_type: Literal["warning", "info", "error"]

    # pylint: disable=R0903
    class Config:
        """
        Configuration settings for the notification schema.

        Attributes:
            allow_population_by_field_name (bool).
            json_encoders (dict).
        """

        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class NotifResponseListSchema(BaseModel):
    """
    NotifResponseListSchema is a schema that represents a list of notification responses.

    Attributes:
        notifications (List[NotifResponseSchema]): A list of notification response schemas.
    """

    notifications: List[NotifResponseSchema]
