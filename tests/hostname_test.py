# -*- coding: utf-8 -*-
"""Test overview/hostname-list endpoint."""

ENDPOINT = "/overview"


def test_get_all_hostnames(client, headers):
    """Test get_all_hostnames."""
    response = client.get(f"{ENDPOINT}/hostname-list", headers=headers)
    response_data = response.json()

    assert response.status_code == 200
    assert isinstance(response_data["hostnames"], list)
    assert all(isinstance(hostname, str) for hostname in response_data["hostnames"])


def test_add_hostname_in_custom_list(client, headers, overview_data_db):
    """Test add_hostname_in_custom_list"""
    _ = overview_data_db
    hostname = "server1"
    response = client.post(
        f"{ENDPOINT}/hostname/custom?hostname={hostname}",
        headers=headers,
        json={"hostname": hostname},
    )
    response_data = response.json()

    assert response.status_code == 200
    assert "hostnames" in response_data
    assert hostname in response_data["hostnames"]


def test_add_existing_hostname_in_custom_list(client, headers, overview_data_db):
    """Test add_existing_hostname_in_custom_list"""
    _ = overview_data_db
    hostname = "server1"
    response = client.post(
        f"{ENDPOINT}/hostname/custom?hostname={hostname}",
        headers=headers,
        json={"hostname": hostname},
    )
    response = client.post(
        f"{ENDPOINT}/hostname/custom?hostname={hostname}",
        headers=headers,
        json={"hostname": hostname},
    )
    response_data = response.json()

    assert response.status_code == 200
    assert "hostnames" in response_data
    assert len(response_data["hostnames"]) == 1
    assert response_data["hostnames"][0] == hostname


def test_add_non_existing_hostname_in_custom_list(client, headers, overview_data_db):
    """Test add_non_existing_hostname_in_custom_list."""
    _ = overview_data_db
    hostname = "non_existing_server"
    response = client.post(
        f"{ENDPOINT}/hostname/custom?hostname={hostname}",
        headers=headers,
        json={"hostname": hostname},
    )
    response_data = response.json()

    assert response.status_code == 404
    assert "detail" in response_data
    assert response_data["detail"] == "Invalid hostname"


def test_get_custom_hostname_list(client, headers, overview_data_db):
    """Test get_custom_hostname_list."""
    _ = overview_data_db
    response = client.get(f"{ENDPOINT}/hostname/custom", headers=headers)
    response_data = response.json()

    assert response.status_code == 200
    assert "hostnames" in response_data
    assert len(response_data["hostnames"]) > 0


def test_delete_custom_hostname_list(client, headers, overview_data_db):
    """Test delete_custom_hostname_list."""
    _ = overview_data_db
    hostname = "server1"
    response = client.delete(f"{ENDPOINT}/hostname/custom/{hostname}", headers=headers)

    assert response.status_code == 200


def test_delete_unexisting_custom_hostname_list(client, headers, overview_data_db):
    """Test delete_unexisting_custom_hostname_list."""
    _ = overview_data_db
    hostname = "server2"
    response = client.delete(f"{ENDPOINT}/hostname/custom/{hostname}", headers=headers)
    response_data = response.json()

    assert response.status_code == 404
    assert "detail" in response_data
    assert response_data["detail"] == "Invalid hostname"
