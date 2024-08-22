# -*- coding: utf-8 -*-
"""handle CRUD operations for notif model. """

from fastapi import HTTPException

from src.gpac_api.app.models.notif import NotifModel
from src.gpac_api.app.schemas.notif import NotifResponseSchema
from src.gpac_api.app.db.database import db
from src.gpac_api.app.utils.logger import logger
from src.gpac_api.app.utils.converters import convert_object_ids, str_to_object_id


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


def find_notif(notif_id: int) -> NotifResponseSchema:
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
    logger.debug("database ok")
    try:
        object_id = str_to_object_id(notif_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="Invalid notification ID format"
        ) from e
    found_notif = collection.find_one({"_id": object_id})
    logger.debug("Found notification %s", found_notif)
    return found_notif
