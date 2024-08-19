# -*- coding: utf-8 -*-
"""Test the main module."""


def test_read_root(client):
    """
    Raises:
        AssertionError: If the response status code is not 200.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Gpac API"
