from fastapi.testclient import TestClient
from main import app
from routers.gender import GenderRepository
import json

client = TestClient(app)


class GenderRepositoryMock:
    def get_all(self):
        return []

    def create(self, gender):
        response = {
            "id": 1,
            "name": "string",
        }
        response.update(gender)
        return response


def test_create():
    app.dependency_overrides[GenderRepository] = GenderRepositoryMock
    gender = {
        "name": "male"
    }

    response = client.post(
        "/gender",
        json.dumps(gender)
    )

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "male"

    app.dependency_overrides = {}


def test_get_all_gender():
    app.dependency_overrides[GenderRepository] = GenderRepositoryMock

    response = client.get("/gender")

    assert response.status_code == 200
    assert response.json() == []

    app.dependency_overrides = {}
