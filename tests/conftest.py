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


# insert test user in test db
def user():
    """
    Create a test user in the database for testing purposes.

    Returns:
        Collection: The database collection reference for the "user" collection.
    """
    user_collection_db = db["user"]
    user_collection_db.insert_one(
        {
            "username": "testuser",
            "password": "testpassword",
            "email": "testemail@testuser.com",
            "description": "testdescription",
        }
    )
    return user_collection_db


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

    result = notif_collection_db.insert_one(
        {
            "recipients": ["string"],
            "gpus": ["string"],
            "mail_content": "string",
            "message_type": "info",
        }
    )

    inserted_id = result.inserted_id

    return notif_collection_db, inserted_id


@pytest.fixture
def headers():
    """
    Fixture that provides authorization headers for testing.

    Returns:
        dict: A dictionary containing the Authorization header with basic credentials.
    """
    user()
    credentials = b64encode("testuser:testpassword".encode()).decode("utf-8")
    return {"Authorization": f"Basic {credentials}"}
