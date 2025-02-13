# -*- coding: utf-8 -*-
"""GPU data schemas."""
from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel

from src.gpac_api.app.models.gpu_data import GpuInfoModel


class GPUDataCreateSchema(BaseModel):
    """
    Represents the schema for creating GPU data entries.

    Args:
        hostname (str)
        gpus (List[GpuInfo])
        timestamp (datetime)
    """

    hostname: str
    gpus: List[GpuInfoModel]
    timestamp: datetime


class GPUDataResponseSchema(BaseModel):
    """
    Represents the schema for GPU data responses.

    Args:
        _id (str)
        hostname (str)
        gpus (List[GpuInfo])
        timestamp (datetime)
    """

    _id: str
    hostname: str
    gpus: List[GpuInfoModel]
    timestamp: datetime

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


class GPUDataResponseListSchema(BaseModel):
    """
    Represents the schema for a list of GPU data responses.
    """

    gpu_data: List[GPUDataResponseSchema]
