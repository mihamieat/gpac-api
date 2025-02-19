# -*- coding: utf-8 -*-
"""Gpac API main module."""

import os

from dotenv import load_dotenv, dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.gpac_api.app.utils.lifespan import lifespan
from src.gpac_api.app.api.endpoints import notif, gpu_data, overview


load_dotenv()
dotenv_config = dotenv_values()
FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", dotenv_config.get("FRONTEND_ORIGIN"))

app = FastAPI(lifespan=lifespan)

origins = list(filter(None, ["http://localhost:3000", FRONTEND_ORIGIN]))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
