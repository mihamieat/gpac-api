# -*- coding: utf-8 -*-
"""date models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DateRangeModel(BaseModel):
    """
    Represents a model for a range of dates

    Attributes:
        start_date (datetime) format: 2023-10-01T00:00:00
        end_date (datetime): 2023-10-01T01:00:00.
    """

    start_date: Optional[datetime]
    end_date: Optional[datetime]
