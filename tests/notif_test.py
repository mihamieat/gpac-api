# -*- coding: utf-8 -*-
"""Test notif endpoint."""
ENDPOINT = "/notif"


def test_get_notif(client, notif_db):
    """Test get notif."""
    _, notif_id = notif_db
    response = client.get(f"{ENDPOINT}/{notif_id}")
    assert response.status_code == 200


def test_create_notif(client):
    """Test create notif."""
    data = {
        "recipients": ["tester@example.com"],
        "gpus": ["GPU1", "GPU2"],
        "mail_content": "Critical GPU usage.",
        "message_type": "info",
    }
    response = client.post(f"{ENDPOINT}", json=data)
    assert response.status_code == 200
    assert response.json() == data
