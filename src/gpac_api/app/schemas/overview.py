# -*- coding: utf-8 -*-
"""Overview data schemas."""
from typing import List

from pydantic import BaseModel


class OverviewCreateSchema(BaseModel):
    """Schema for creating overview data.
    Represents the structure for creating overview data.
    """

    hostname: str
    gpu_data: List[int]
    percentage: float
