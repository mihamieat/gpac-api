# -*- coding: utf-8 -*-
"""Test overview endpoint."""

ENDPOINT = "/overview"


def test_create_overview_normal_case(client, headers):
    """Test create_overview with normal data."""
    overview_data = {
        "hostname": "server1",
        "gpu_data": [
            {"percentage": 90, "timestamp": "2022-01-01T12:00:00"},
            {"percentage": 80, "timestamp": "2022-01-01T13:00:00"},
        ],
        "percentage": {"percentage": 80, "timestamp": "2022-01-01T13:00:00"},
        "active_users": 1,
    }
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 200


def test_create_overview_unauthorized(client):
    """Test create_overview without authorization."""
    overview_data = {
        "hostname": "server1",
        "gpu_data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "percentage": 10,
        "active_users": 1,
    }
    response = client.post(ENDPOINT, json=overview_data)
    assert response.status_code == 401


def test_create_overview_gpu_data_edge_cases(client, headers):
    """Test create_overview with edge cases for gpu_data."""
    # Empty list (valid case)
    overview_data = {
        "hostname": "server1",
        "gpu_data": [],
        "percentage": {"percentage": 50, "timestamp": "2022-01-01T13:00:00"},
        "active_users": 1,
    }
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 200

    # Very large list
    overview_data["gpu_data"] = [
        {"percentage": i % 101, "timestamp": f"2022-01-01T{i % 24:02d}:00:00"}
        for i in range(500)  # Reduce if needed
    ]
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 200

    # Negative values (should be invalid)
    overview_data["gpu_data"] = [
        {"percentage": -1, "timestamp": "2022-01-01T12:00:00"},
        {"percentage": -5, "timestamp": "2022-01-01T13:00:00"},
    ]
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 422  # Assuming negative values are not allowed


def test_create_overview_percentage_edge_cases(client, headers):
    """Test create_overview with edge cases for percentage."""
    base_data = {
        "hostname": "server1",
        "gpu_data": [
            {"percentage": 20, "timestamp": "2022-01-01T12:00:00"},
            {"percentage": 40, "timestamp": "2022-01-01T13:00:00"},
        ],
        "active_users": 1,
    }

    # Test negative percentage (should fail)
    overview_data = {
        **base_data,
        "percentage": {"percentage": -10, "timestamp": "2022-01-01T14:00:00"},
    }
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 422

    # Test zero percentage (valid case)
    overview_data["percentage"] = {"percentage": 0, "timestamp": "2022-01-01T14:00:00"}
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 200

    # Test 100 percentage (valid case)
    overview_data["percentage"] = {
        "percentage": 100,
        "timestamp": "2022-01-01T14:00:00",
    }
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 200

    # Test percentage > 100 (should fail)
    overview_data["percentage"] = {
        "percentage": 150,
        "timestamp": "2022-01-01T14:00:00",
    }
    response = client.post(ENDPOINT, headers=headers, json=overview_data)
    assert response.status_code == 422
