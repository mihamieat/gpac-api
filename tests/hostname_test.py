# -*- coding: utf-8 -*-
"""Test overview/hostname-list endpoint."""

ENDPOINT = "/overview/hostname-list"


def test_get_all_hostnames(client, headers):
    """Test get_all_hostnames."""
    response = client.get(ENDPOINT, headers=headers)
    response_data = response.json()

    assert response.status_code == 200
    assert isinstance(response_data["hostnames"], list)
    assert all(isinstance(hostname, str) for hostname in response_data["hostnames"])
