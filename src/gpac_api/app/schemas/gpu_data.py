# -*- coding: utf-8 -*-
"""GPU data schemas."""
from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel


class GpuInfoSchema(BaseModel):
    """
    Represents the model for GPU information.

    Args:
        gpu_name (str): The name of the GPU.
        load (float): The current load percentage of the GPU.
        memory (float): The total memory available on the GPU.
    """

    gpu_name: str
    gpu_id: str
    fan_speed: int
    temperature: int
    performance: str
    power_used: int
    power_total: int
    memory_used: int
    memory_total: int
    gpu_utilization: int


class GPUDataCreateSchema(BaseModel):
    """
    Represents the schema for creating GPU data entries.

    Args:
        hostname (str)
        gpus (List[GpuInfo])
        timestamp (datetime)
    """

    hostname: str
    gpus: List[GpuInfoSchema]
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
    gpus: List[GpuInfoSchema]
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
