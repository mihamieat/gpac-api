# -*- coding: utf-8 -*-
"""gpu data api endpoint modules."""
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import HTTPBasicCredentials

from src.gpac_api.app.crud.gpu_data import (
    create_gpu_data,
    get_gpu_data_by_time_interval,
)
from src.gpac_api.app.schemas.gpu_data import (
    GPUDataCreateSchema,
    GPUDataResponseSchema,
    GPUDataResponseListSchema,
)
from src.gpac_api.app.models.date_models import DateRangeModel
from src.gpac_api.app.utils.security import verify_credentials, security

router = APIRouter()


@router.post("/", response_model=GPUDataResponseSchema)
def new_gpu_data(
    gpu_data: GPUDataCreateSchema,
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    """
    Creates a new GPU data entry in the system.

    Args:
        gpu_data (GPUDataCreateSchema)
        credentials (HTTPBasicCredentials)
    Returns:
        GPUDataResponseSchema.

    Raises:
        HTTPException: If the credentials are invalid \
or the GPU data creation fails.

    Examples:
        >>> response = new_gpu_data(gpu_data, credentials)
        >>> assert response is not None
    """
    verify_credentials(credentials)
    return create_gpu_data(gpu_data)


@router.get("/", response_model=GPUDataResponseListSchema)
def get_gpu_data(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    start_date: Optional[str] = Query(
        None, description="Start date in ISO 8601 format (YYYY-MM-DDTHH:MM:SS)"
    ),
    end_date: Optional[str] = Query(
        None, description="Start date in ISO 8601 format (YYYY-MM-DDTHH:MM:SS)"
    ),
):
    """
    Retrieve all GPU data.

    Args:
        credentials (HTTPBasicCredentials)

    Returns:
        GPUDataResponseListSchema
    """
    verify_credentials(credentials)
    try:
        DateRangeModel(start_date=start_date, end_date=end_date)
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid datetime format") from e
    return get_gpu_data_by_time_interval(start_date, end_date)
