# -*- coding: utf-8 -*-
"""handle CRUD operations for overview data model."""
from typing import Optional
from src.gpac_api.app.schemas.overview import (
    OverviewCreateSchema,
    OverviewResponseSchema,
)
from src.gpac_api.app.db.database import db
from src.gpac_api.app.utils.converters import convert_object_ids


def create_overview(overview_data: OverviewCreateSchema) -> OverviewResponseSchema:
    """
    Creates a new overview entry in the database.

    Args:
        overview_data (OverviewCreateSchema)

    Returns:
        OverviewResponseSchema
    """
    collection = db.overview_data
    document = overview_data.model_dump()
    new_overview_data = collection.insert_one(overview_data.model_dump())
    document["_id"] = new_overview_data.inserted_id
    return convert_object_ids(document)


def get_latest_overview(hostname: str) -> Optional[OverviewResponseSchema]:
    """
    Retrieves the latest overview entry from the database.

    Returns:
        Optional[OverviewResponseSchema]: The latest overview entry or None if no entry is found.
    """
    collection = db.overview_data
    latest_overview_data = (
        collection.find({"hostname": hostname})
        .sort("percentage.timestamp", -1)
        .limit(1)
    )

    if latest_overview_list := list(latest_overview_data):
        return convert_object_ids(latest_overview_list[0])
    return None
