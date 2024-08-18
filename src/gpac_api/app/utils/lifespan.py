# -*- coding: utf-8 -*-
"""Lifspan module."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.gpac_api.app.db.database import client
from src.gpac_api.app.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application by setting up and tearing down resources.

    Args:
        app (FastAPI): The FastAPI application instance.
        client: The database client to be used by the application.

    Yields:
        None: Control is yielded back to the application during its lifespan.

    Raises:
        None
    """
    app.state.client = client
    app.state.db = client.gpac_db_test
    logger.debug("Logged to database")

    yield

    client.close()
