# -*- coding: utf-8 -*-
"""overview api endpoint modules."""
from fastapi import APIRouter, Depends, Query

from src.gpac_api.app.crud.overview import (
    create_overview,
    get_latest_overview,
    get_all_hostnames,
    add_to_custom_hostname_list,
    get_custom_hostname_list,
    del_hostname_from_custom_list,
)
from src.gpac_api.app.schemas.overview import (
    OverviewCreateSchema,
    OverviewResponseSchema,
    HostnamesResponseSchema,
)
from src.gpac_api.app.utils.security import require_credentials


router = APIRouter()


@router.post(
    "/",
    response_model=OverviewResponseSchema,
    dependencies=[Depends(require_credentials)],
)
def new_overview(
    overview: OverviewCreateSchema,
):
    """
    Creates a new overview entry in the system.

    Returns:
        OverviewResponseSchema.

    Raises:
        None
    """
    return create_overview(overview)


@router.get(
    "/",
    response_model=OverviewResponseSchema,
    dependencies=[Depends(require_credentials)],
)
def get_overview(
    hostname: str = Query(..., description="Hostname to get data from"),
):
    """
    Retrieves the latest overview entry.

    Returns:
        OverviewResponseSchema.

    Raises:
        None
    """
    return get_latest_overview(hostname)


@router.get(
    "/hostname-list",
    response_model=HostnamesResponseSchema,
    dependencies=[Depends(require_credentials)],
)
def get_hostnames():
    """
    Retrieves all unique hostnames from the database.

    Returns:
        HostnamesResponseSchema.
    """
    return get_all_hostnames()


@router.post(
    "/hostname/custom",
    response_model=HostnamesResponseSchema,
    dependencies=[Depends(require_credentials)],
)
def add_hostname_in_custom_list(
    hostname: str,
):
    """
    Adds a new hostname to the database.

    Returns:
        HostnamesResponseSchema.

    Raises:
        None
    """
    return add_to_custom_hostname_list(hostname)


@router.get(
    "/hostname/custom",
    response_model=HostnamesResponseSchema,
    dependencies=[Depends(require_credentials)],
)
def get_hostnames_from_custom_list():
    """
    Retrieves all unique hostnames from the database.

    Returns:
        HostnamesResponseSchema.
    """
    return get_custom_hostname_list()


@router.delete(
    "/hostname/custom/{hostname}", dependencies=[Depends(require_credentials)]
)
def remove_hostname_from_custom_list(
    hostname: str,
):
    """
    Removes a hostname from the database.

    Returns:
        None.
    """
    return del_hostname_from_custom_list(hostname)
