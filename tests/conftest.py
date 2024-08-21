# -*- coding: utf-8 -*-
"""Test the main module."""

import os

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
async def notif_db():
    """
    Sets up a notification collection in the database for testing purposes.

    Returns:
        Collection, ObjectId: The notification collection from the database and the\
 inserted document's ID.
    """
    notif_collection_db = db["notif"]

    # Insert a document and await the result
    result = await notif_collection_db.insert_one(
        {
            "recipients": ["string"],
            "gpus": ["string"],
            "mail_content": "string",
            "message_type": "info",
        }
    )

    # Get the inserted document's ID
    inserted_id = result.inserted_id

    # Return the collection and the inserted document's ObjectId
    return notif_collection_db, inserted_id
