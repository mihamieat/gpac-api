# -*- coding: utf-8 -*-
"""Test the main module."""
from fastapi.testclient import TestClient
from src.gpac_api.app.main import app


client = TestClient(app)


def test_read_main():
    """
    Raises:
        AssertionError: If the response status code is not 200.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Gpac API"
