# -*- coding: utf-8 -*-
"""Test gpu_data endpoint."""
from datetime import datetime, timedelta


ENDPOINT = "/gpu_data"


def test_get_gpu_data(client, gpu_data_db, headers):
    """Test get_gpu_data."""
    _ = gpu_data_db
    response = client.get(ENDPOINT, headers=headers)
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data["gpu_data"]) == 2
    assert "hostname" in response_data["gpu_data"][0]
    assert "gpus" in response_data["gpu_data"][0]
    assert "timestamp" in response_data["gpu_data"][0]


def test_get_gpu_data_unauthorized(client):
    """Test unauthorized access to get_gpu_data."""
    response = client.get(ENDPOINT)
    assert response.status_code == 401


def test_get_gpu_data_with_dates(client, gpu_data_db, headers):
    """Test get_gpu_data."""
    _ = gpu_data_db
    start_date = (datetime.now() - timedelta(days=1)).isoformat()
    end_date = (datetime.now()).isoformat()
    response = client.get(
        f"{ENDPOINT}/?start_date={start_date}&end_date={end_date}", headers=headers
    )

    assert response.status_code == 200


def test_get_gpu_data_with_start_date(client, gpu_data_db, headers):
    """Test get_gpu_data."""
    _ = gpu_data_db
    start_date = (datetime.now() - timedelta(days=1)).isoformat()
    response = client.get(f"{ENDPOINT}/?start_date={start_date}", headers=headers)

    assert response.status_code == 200


def test_get_gpu_data_with_end_date(client, gpu_data_db, headers):
    """Test get_gpu_data."""
    _ = gpu_data_db
    end_date = (datetime.now()).isoformat()
    response = client.get(f"{ENDPOINT}/?end_date={end_date}", headers=headers)

    assert response.status_code == 200


def test_get_gpu_data_with_wron_date_format(client, gpu_data_db, headers):
    """Test get_gpu_data."""
    _ = gpu_data_db
    response = client.get(f"{ENDPOINT}/?start_date=23-07", headers=headers)

    assert response.status_code == 400


def test_create_gpu_data(client, headers):
    """Test create_gpu_data."""
    gpu_data = {
        "hostname": "server1",
        "gpus": [
            {
                "gpu_name": "string",
                "gpu_id": "string",
                "fan_speed": 51,
                "temperature": 32,
                "performance": "string",
                "power_used": 22,
                "power_total": 77,
                "memory_used": 324,
                "memory_total": 235,
                "gpu_utilization": 70,
            },
            {
                "gpu_name": "string",
                "gpu_id": "string",
                "fan_speed": 20,
                "temperature": 20,
                "performance": "string",
                "power_used": 10,
                "power_total": 20,
                "memory_used": 40,
                "memory_total": 50,
                "gpu_utilization": 60,
            },
        ],
        "timestamp": datetime.now().isoformat(),
    }
    response = client.post(ENDPOINT, headers=headers, json=gpu_data)
    assert response.status_code == 200
