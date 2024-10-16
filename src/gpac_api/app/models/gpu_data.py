# -*- coding: utf-8 -*-
"""gpu_data models."""

from datetime import datetime
from typing import List

from pydantic import BaseModel


class GpuInfoModel(BaseModel):
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


class GpuDataModel(BaseModel):
    """
    Represents the model for GPU data.

    Args:
        hostname (str)
        gpus (List[GpuInfo])
        timestamp (datetime)
    """

    hostname: str
    gpus: List[GpuInfoModel]
    timestamp: datetime
