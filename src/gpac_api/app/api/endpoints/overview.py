# -*- coding: utf-8 -*-
"""overview api endpoint modules."""
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from fastapi.security import HTTPBasicCredentials

from src.gpac_api.app.crud.overview import (
    create_overview,
    get_latest_overview,
    get_all_hostnames,
)
from src.gpac_api.app.schemas.overview import (
    OverviewCreateSchema,
    OverviewResponseSchema,
    HostnamesResponseSchema,
)
from src.gpac_api.app.utils.security import verify_credentials, security


router = APIRouter()


@router.post("/", response_model=OverviewResponseSchema)
def new_overview(
    overview: OverviewCreateSchema,
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    """
    Creates a new overview entry in the system.

    Returns:
        OverviewResponseSchema.

    Raises:
        None
    """
    verify_credentials(credentials)
    return create_overview(overview)


@router.get("/", response_model=OverviewResponseSchema)
def get_overview(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    hostname: str = Query(..., description="Hostname to get data from"),
):
    """
    Retrieves the latest overview entry.

    Returns:
        OverviewResponseSchema.

    Raises:
        None
    """
    verify_credentials(credentials)
    return get_latest_overview(hostname)


@router.get("/hostname-list", response_model=HostnamesResponseSchema)
def get_hostnames(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    """
    Retrieves all unique hostnames from the database.

    Returns:
        HostnamesResponseSchema.
    """
    verify_credentials(credentials)
    return get_all_hostnames()
