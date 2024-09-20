# -*- coding: utf-8 -*-
"""Test notif endpoint."""
ENDPOINT = "/notif"


def test_get_notif(client, notif_db, headers):
    """Test get notif."""
    _, notif_id = notif_db
    response = client.get(f"{ENDPOINT}/{notif_id}", headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert "string" in response_data["recipients"]
    assert "string" in response_data["gpus"]
    assert "string" == response_data["mail_content"]


def test_unauthenticated_user_notif(client, notif_db):
    """Test not authenticated user."""
    _, notif_id = notif_db
    response = client.get(f"{ENDPOINT}/{notif_id}")
    response_data = response.json()
    assert response.status_code == 401
    assert response_data == {"detail": "Not authenticated"}


def test_unauthorized_user_notif(client, notif_db):
    """Test unauthorized user."""
    _, notif_id = notif_db
    response = client.get(
        f"{ENDPOINT}/{notif_id}",
        headers={"Authorization": "Basic c3RhbmxleWpvYnNvbjpzd29yZGZpZw=="},
    )
    response_data = response.json()
    assert response.status_code == 401
    assert response_data == {"detail": "Incorrect username or password"}


def test_invalid_auth_user_notif(client, notif_db):
    """Test invalid credentials user."""
    _, notif_id = notif_db
    response = client.get(
        f"{ENDPOINT}/{notif_id}", headers={"Authorization": "Basic aaa"}
    )
    response_data = response.json()
    assert response.status_code == 401
    assert response_data == {"detail": "Invalid authentication credentials"}


def test_notice_not_found(client, headers):
    """Test notice not found."""
    response = client.get(f"{ENDPOINT}/66c72cb4ddce5033850626b7", headers=headers)
    assert response.status_code == 404
    response_data = response.json()
    assert "Notif not found" == response_data["detail"]


def test_notif_wrong_id_format(client, headers):
    """Test notif wrong id format."""
    invalid_ids = ["-1", "9" * 20, "abc123", "!@#$%"]
    # sourcery skip: no-loop-in-tests
    for inv_id in invalid_ids:
        response = client.get(f"{ENDPOINT}/{inv_id}", headers=headers)
        response_data = response.json()
        assert response.status_code == 400
        assert response_data["detail"] == "Invalid notification ID format"


def test_create_notif(client, notif_db, headers):
    """Test create notif."""
    data = {
        "recipients": ["tester@example.com"],
        "gpus": ["GPU1", "GPU2"],
        "mail_content": "Critical GPU usage.",
        "message_type": "info",
    }
    response = client.post(f"{ENDPOINT}", json=data, headers=headers)
    assert response.status_code == 200
    db_notif, _ = notif_db
    create_notif = db_notif.find_one({"recipients": data["recipients"]})
    assert create_notif is not None
    assert create_notif["recipients"] == data["recipients"]
    assert create_notif["gpus"] == data["gpus"]
    assert create_notif["mail_content"] == data["mail_content"]
    assert create_notif["message_type"] == data["message_type"]


def test_delete_notif(client, notif_db, headers):
    """Test delete notif."""
    _, notif_id = notif_db
    response = client.delete(f"{ENDPOINT}/{notif_id}", headers=headers)
    not_found = client.get(
        f"{ENDPOINT}/{notif_id}",
        headers=headers,
    )
    assert response.status_code == 200
    assert not_found.status_code == 404
