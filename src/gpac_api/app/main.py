# -*- coding: utf-8 -*-
"""Gpac API main module."""

from fastapi import FastAPI
from src.gpac_api.app.utils.lifespan import lifespan
from src.gpac_api.app.api.endpoints import notif, gpu_data, overview


app = FastAPI(lifespan=lifespan)

app.include_router(notif.router, prefix="/notif", tags=["notif"])
app.include_router(gpu_data.router, prefix="/gpu_data", tags=["gpu_data"])
app.include_router(overview.router, prefix="/overview", tags=["overview"])


@app.get("/")
def read_root() -> dict:
    """
    Returns a welcome message and the creators of the Gpac API.

    Args:
        None

    Returns:
        dict: A dictionary containing a welcome message and a list of creators' email addresses.
    """
    return {
        "message": "Welcome to Gpac API",
        "creators": ["r.miham@yahoo.com", "stephan.vujasinovic@gmail.com"],
    }
