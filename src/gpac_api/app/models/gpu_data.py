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
    power_usage_min: int
    power_usage_max: int
    memory_used: int
    memory_total: int
    gpu_utilization: int


class GpuDataModel(BaseModel):
    """
    Represents the model for GPU data.

    Args:
        server_name (str)
        gpus (List[GpuInfo])
        timestamp (datetime)
    """

    server_name: str
    gpus: List[GpuInfoModel]
    timestamp: datetime
