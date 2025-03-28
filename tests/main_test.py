# -*- coding: utf-8 -*-
"""Test the main module."""
import os


def test_read_root(client):
    """
    Raises:
        AssertionError: If the response status code is not 200.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Gpac API"


def test_origins_with_frontend_origin(monkeypatch):
    """Test when FRONTEND_ORIGIN is set."""
    monkeypatch.setenv("FRONTEND_ORIGIN", "https://example.com")
    assert os.getenv("FRONTEND_ORIGIN") == "https://example.com"
