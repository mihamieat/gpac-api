# -*- coding: utf-8 -*-
"""Test the main module."""

import pytest
from fastapi.testclient import TestClient

from src.gpac_api.app.utils.testenv import TESTING  # noqa pylint: disable=W0611
from src.gpac_api.app.main import app
from src.gpac_api.app.db.database import db


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
def notif_db():
    """
    Sets up a notification collection in the database for testing purposes.

    Returns:
        Collection, ObjectId: The notification collection from the database and the\
 inserted document's ID.
    """
    notif_collection_db = db["notif"]

    # Insert a document and await the result
    result = notif_collection_db.insert_one(
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
