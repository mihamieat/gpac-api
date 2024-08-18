# -*- coding: utf-8 -*-
"""notif models."""

from typing import List, Literal

from pydantic import BaseModel


class NotifModel(BaseModel):
    """
    Notif Model.
    Attributes:
        recipients (List[str]): A list of email addresses .
        gpus (List[str]): A list of GPU identifiers.
        timestamp (datetime): The timestamp indicating when the notification was created.
        mail_content (str): The content of the mails.
        message_type (Literal['warning', 'info', 'error']).
    """

    recipients: List[str]
    gpus: List[str]
    # timestamp: datetime
    mail_content: str
    message_type: Literal["warning", "info", "error"]
