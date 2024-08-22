# -*- coding: utf-8 -*-
"""Test notif endpoint."""
ENDPOINT = "/notif"


def test_get_notif(client, notif_db):
    """Test get notif."""
    _, notif_id = notif_db
    response = client.get(f"{ENDPOINT}/{notif_id}")
    assert response.status_code == 200


def test_notice_not_found(client):
    """Test notice not found."""
    response = client.get(f"{ENDPOINT}/66c72cb4ddce5033850626b7")
    assert response.status_code == 404


def test_notif_wrong_id_format(client):
    """Test notif wrong id format."""
    response = client.get(f"{ENDPOINT}/wrong-id-format")
    assert response.status_code == 400


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
