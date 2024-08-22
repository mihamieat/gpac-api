# -*- coding: utf-8 -*-
"""notif api endpoint modules."""

from fastapi import APIRouter, HTTPException

from src.gpac_api.app.crud.notif import create_notif, find_notif
from src.gpac_api.app.schemas.notif import NotifCreateSchema, NotifResponseSchema
from src.gpac_api.app.utils.logger import logger


router = APIRouter()


@router.post("/", response_model=NotifResponseSchema)
def new_notif(notif: NotifCreateSchema):
    """
    Creates a new notification based on the provided notification data.

    Args:
        notif (NotifCreateSchema).

    Returns:
        NotifResponseSchema: The response schema representing the created notification.

    Raises:
        None
    """
    return create_notif(notif)


@router.get("/{notif_id}", response_model=NotifResponseSchema)
def get_notif(notif_id: str):
    """
    Retrieves a notification by its identifier.

    Args:
        notif_id (str): The unique identifier of the notification to be retrieved.

    Returns:
        NotifResponseSchema: The response schema representing the retrieved notification.

    Raises:
        HTTPException: Raised if the provided notification ID format is invalid.
    """
    logger.debug("notif_id: %s", notif_id)
    notif = find_notif(notif_id)
    if notif is None:
        raise HTTPException(status_code=404, detail="Notif not found")
    return notif
