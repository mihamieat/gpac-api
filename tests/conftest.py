# -*- coding: utf-8 -*-
"""Test the main module."""

import os

from bson import ObjectId
import pytest
from fastapi.testclient import TestClient

from src.gpac_api.app import main
from src.gpac_api.app.db import database

os.environ["TESTING"] = "TRUE"

app = main.app
db = database.db


@pytest.fixture
def client():
    """
    Provides a test client for the FastAPI application.

    Returns:
        TestClient: An instance of the FastAPI test client.
    """

    return TestClient(app)


# notifs
@pytest.fixture
def notif_collection():
    """
    Sets up a notification collection in the database for testing purposes.

    Returns:
        Collection: The notification collection from the database.
    """

    notif_collection_db = db["notif"]
    notif_collection_db.insert_one(
        {
            "_id": ObjectId(1),
            "recipients": ["string"],
            "gpus": ["string"],
            "mail_content": "string",
            "message_type": "info",
        }
    )
