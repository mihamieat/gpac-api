# -*- coding: utf-8 -*-
"""handle CRUD operations for notif model. """

from src.gpac_api.app.models.notif import NotifModel
from src.gpac_api.app.schemas.notif import NotifResponseSchema
from src.gpac_api.app.db.database import db
from src.gpac_api.app.utils.logger import logger
from src.gpac_api.app.utils.converters import (
    convert_object_ids,
    validate_object_ids,
)


def create_notif(notif: NotifModel) -> NotifResponseSchema:
    """
    Creates a new notification in the database.

    Args:
        notif (NotifModel).

    Returns:
        NotifResponseSchema: The response schema representing the created notification.

    Raises:
        None
    """

    collection = db.notif
    new_notif = collection.insert_one(notif.model_dump())
    created_notif = collection.find_one({"_id": new_notif.inserted_id})
    created_item_dict = convert_object_ids(created_notif)
    logger.debug("Created notif: %s", created_item_dict)
    return created_item_dict


def find_notif(notif_id: str) -> NotifResponseSchema:
    """
    Retrieves notification data from the database by its identifier.

    Args:
        notif_id (int): The unique identifier of the notification to be retrieved.

    Returns:
        NotifResponseSchema: The response schema representing the retrieved notification.

    Raises:
        None
    """
    collection = db.notif
    object_id = validate_object_ids(notif_id)
    found_notif = collection.find_one({"_id": object_id})
    logger.debug("Found notification %s", found_notif)
    return found_notif


def del_notif(notif_id: str):
    """Delete a notification from the database.

    Args:
        notif_id (str): The unique identifier of the notification to be deleted.

    Returns:
        None

    Raises:
        ValueError: If the provided notif_id is invalid.
    """
    collection = db.notif
    object_id = validate_object_ids(notif_id)
    collection.delete_one({"_id": object_id})
