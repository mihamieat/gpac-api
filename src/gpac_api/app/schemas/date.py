# -*- coding: utf-8 -*-
"""date schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DateRangeSchema(BaseModel):
    """
    Represents a model for a range of dates

    Attributes:
        start_date (datetime) format: 2023-10-01T00:00:00
        end_date (datetime): 2023-10-01T01:00:00.
    """

    start_date: Optional[datetime] = Field(default=None)
    end_date: Optional[datetime] = Field(default=None)
