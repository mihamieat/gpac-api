# -*- coding: utf-8 -*-
"""Overview data schemas."""
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class PercentageDataSchema(BaseModel):
    """Schema for percentage validation.
    Represents the structure for validating percentage.
    """

    percentage: float = Field(
        ge=0, le=100, description="Percentage value between 0 and 100"
    )
    timestamp: datetime


class OverviewCreateSchema(BaseModel):
    """Schema for creating overview data.
    Represents the structure for creating overview data.
    """

    hostname: str
    gpu_data: List[PercentageDataSchema]
    percentage: PercentageDataSchema
    active_users: int


class OverviewResponseSchema(BaseModel):
    """Schema for overview data responses.
    Represents the structure for overview data responses.
    """

    _id: str
    hostname: str
    gpu_data: List[PercentageDataSchema]
    percentage: PercentageDataSchema
    active_users: int
