# -*- coding: utf-8 -*-
"""handle CRUD operations for gpu_data model. """

from dateutil import parser

from src.gpac_api.app.models.gpu_data import GpuDataModel
from src.gpac_api.app.schemas.gpu_data import (
    GPUDataResponseSchema,
    GPUDataResponseListSchema,
)
from src.gpac_api.app.db.database import db
from src.gpac_api.app.utils.converters import convert_object_ids


def create_gpu_data(gpu_data: GpuDataModel) -> GPUDataResponseSchema:
    """
    Creates a new GPU data entry in the database.

    Args:
        gpu_data (GpuDataModel)

    Returns:
        GPUDataResponseSchema
    """
    collection = db.gpu_data
    new_gpu_data = collection.insert_one(gpu_data.model_dump())
    created_gpu_data = collection.find_one({"_id": new_gpu_data.inserted_id})
    return convert_object_ids(created_gpu_data)


def get_gpu_data_by_time_interval(start_date, end_date):
    """
    Retrieves GPU data within a specified time interval.

    Args:
        start_date (Union[str, datetime])
        end_date (Union[str, datetime])

    Returns:
        GPUDataResponseListSchema

    Raises:
        ValueError: If the provided date strings cannot be parsed into valid datetime objects.
    """
    collection = db.gpu_data
    query = {}

    if isinstance(start_date, str):
        start_date = parser.isoparse(start_date)
    if isinstance(end_date, str):
        end_date = parser.isoparse(end_date)

    if start_date and end_date:
        query["timestamp"] = {"$gte": start_date, "$lte": end_date}
    elif start_date:
        query["timestamp"] = {"$gte": start_date}
    elif end_date:
        query["timestamp"] = {"$lte": end_date}

    result = list(collection.find(query))
    gpu_data = [GPUDataResponseSchema(**gpu_data) for gpu_data in result]
    return GPUDataResponseListSchema(gpu_data=gpu_data)
