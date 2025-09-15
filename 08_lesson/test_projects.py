import pytest
from api_client import YougileClient


@pytest.fixture
def client(base_url, headers):
    return YougileClient(base_url, headers)


# ---------- [POST] /projects ----------
def test_create_project_positive(client):
    payload = {"name": "Test Project"}
    response = client.create_project(payload)
    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]


def test_create_project_negative(client):
    payload = {}  # без обязательных полей
    response = client.create_project(payload)
    assert response.status_code == 400


# ---------- [PUT] /projects/{id} ----------
def test_update_project_positive(client):
    # сначала создаем проект
    project = client.create_project({"name": "Initial"}).json()
    project_id = project["id"]

    payload = {"name": "Updated Name"}
    response = client.update_project(project_id, payload)
    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]


def test_update_project_negative(client):
    payload = {"name": "Should Fail"}
    response = client.update_project("non-existing-id", payload)
    assert response.status_code == 404


# ---------- [GET] /projects/{id} ----------
def test_get_project_positive(client):
    project = client.create_project({"name": "To Read"}).json()
    response = client.get_project(project["id"])
    assert response.status_code == 200
    assert response.json()["id"] == project["id"]


def test_get_project_negative(client):
    response = client.get_project("wrong-id")
    assert response.status_code == 404
