# -*- coding: utf-8 -*-
"""Test the main module."""

from base64 import b64encode
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

    test_client = TestClient(app)
    yield test_client
    test_client.close()


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


@pytest.fixture
def headers():
    """
    Fixture that provides authorization headers for testing.

    Returns:
        dict: A dictionary containing the Authorization header with basic credentials.
    """
    credentials = b64encode("eteph:$wordfi$h".encode()).decode("utf-8")
    return {"Authorization": f"Basic {credentials}"}
