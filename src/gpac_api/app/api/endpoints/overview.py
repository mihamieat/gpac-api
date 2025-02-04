# -*- coding: utf-8 -*-
"""overview api endpoint modules."""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials

from src.gpac_api.app.crud.overview import create_overview
from src.gpac_api.app.models.overview import OverviewModel
from src.gpac_api.app.schemas.overview import OverviewCreateSchema
from src.gpac_api.app.utils.security import verify_credentials, security


router = APIRouter()


@router.post("/", response_model=OverviewModel)
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
