# -*- coding: utf-8 -*-
"""handle CRUD operations for overview data model."""
from typing import Optional

from fastapi import HTTPException

from src.gpac_api.app.schemas.overview import (
    OverviewCreateSchema,
    OverviewResponseSchema,
    HostnamesResponseSchema,
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
    new_overview_data = collection.insert_one(document)
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


def get_all_hostnames() -> HostnamesResponseSchema:
    """
    Retrieves all unique hostnames from the overview data.

    Returns:
        List[str]: A list of unique hostnames.
    """
    collection = db.overview_data
    results = list(collection.distinct("hostname"))
    return HostnamesResponseSchema(hostnames=results)


def add_to_custom_hostname_list(hostname: str) -> HostnamesResponseSchema:
    """Adds a hostname to a custom list in the database."""

    if hostname not in get_all_hostnames().hostnames:
        raise HTTPException(status_code=404, detail="Invalid hostname")

    collection = db.custom_hostnames
    if not collection.find_one({"hostname": hostname}):
        document = {"hostname": hostname}
        document["_id"] = collection.insert_one(document).inserted_id

    return HostnamesResponseSchema(hostnames=[hostname])


def get_custom_hostname_list() -> HostnamesResponseSchema:
    """
    Retrieves the custom hostname list from the database.

    Returns:
        HostnamesResponseSchema
    """
    collection = db.custom_hostnames
    results = list(collection.find())
    return HostnamesResponseSchema(hostnames=[result["hostname"] for result in results])


def del_hostname_from_custom_list(hostname: str) -> HostnamesResponseSchema:
    """
    Removes a hostname from the custom list in the database.

    Returns:
        HostnamesResponseSchema
    """
    collection = db.custom_hostnames
    if not collection.find_one({"hostname": hostname}):
        raise HTTPException(status_code=404, detail="Invalid hostname")
    collection.delete_one({"hostname": hostname})
