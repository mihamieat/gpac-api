# -*- coding: utf-8 -*-
"""handle CRUD operations for overview data model."""
from src.gpac_api.app.models.overview import OverviewModel
from src.gpac_api.app.schemas.overview import OverviewCreateSchema
from src.gpac_api.app.db.database import db
from src.gpac_api.app.utils.converters import convert_object_ids


def create_overview(overview_data: OverviewCreateSchema) -> OverviewModel:
    """
    Creates a new overview entry in the database.

    Args:
        overview_data (OverviewCreateSchema)

    Returns:
        OverviewModel
    """
    collection = db.overview_data
    document = overview_data.model_dump()
    new_overview_data = collection.insert_one(overview_data.model_dump())
    document["_id"] = new_overview_data.inserted_id
    return convert_object_ids(document)
