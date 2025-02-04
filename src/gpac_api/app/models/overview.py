# -*- coding: utf-8 -*-
"""Overview data models."""

from typing import List

from pydantic import BaseModel


class OverviewModel(BaseModel):
    """
    Represents the model of Overview data.
    Args:
        _id (str): The unique identifier of the overview data.
        hostname (str): The hostname of the system.
        gpu_data (List[int]): A list of GPU data points.
        percentage (float): The overall system performance percentage.
    """

    _id: str
    hostname: str
    gpu_data: List[int]
    percentage: float
