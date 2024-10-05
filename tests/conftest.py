# -*- coding: utf-8 -*-
"""Test the main module."""

from datetime import datetime

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
def gpu_data_db():
    """Setup gpu_data colleciton."""
    gpu_data_collection = db["gpu_data"]
    gpu_data = [
        {
            "server_name": "server1",
            "gpus": [
                {
                    "gpu_name": "string",
                    "gpu_id": "string",
                    "fan_speed": 50,
                    "temperature": 34,
                    "performance": "string",
                    "power_usage_min": 23,
                    "power_usage_max": 78,
                    "memory_used": 3245,
                    "memory_total": 2345,
                    "gpu_utilization": 50,
                },
                {
                    "gpu_name": "string",
                    "gpu_id": "string",
                    "fan_speed": 10,
                    "temperature": 10,
                    "performance": "string",
                    "power_usage_min": 10,
                    "power_usage_max": 10,
                    "memory_used": 10,
                    "memory_total": 10,
                    "gpu_utilization": 10,
                },
            ],
            "timestamp": datetime.now().isoformat(),
        },
        {
            "server_name": "server2",
            "gpus": [
                {
                    "gpu_name": "string",
                    "gpu_id": "string",
                    "fan_speed": 40,
                    "temperature": 40,
                    "performance": "string",
                    "power_usage_min": 40,
                    "power_usage_max": 40,
                    "memory_used": 40,
                    "memory_total": 40,
                    "gpu_utilization": 60,
                }
            ],
            "timestamp": datetime.now().isoformat(),
        },
    ]
    gpu_data_collection.insert_many(gpu_data)
    return gpu_data_collection


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
