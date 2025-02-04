# -*- coding: utf-8 -*-
"""Test overview endpoint."""

ENDPOINT = "/overview"


def test_create_overview(client, headers):
    """Test create_overview."""
    overview_data = {
        "hostname": "server1",
        "gpu_data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "percentage": 10,
    }
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 200
