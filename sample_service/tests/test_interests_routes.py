from fastapi.testclient import TestClient
from main import app
from routers.interests import InterestsRepository
import json

client = TestClient(app)


class InterestsRepositoryMock:
    def create(self, interests):
        response = {
            "id": 0,
            "name": "string",
        }
        response.update(interests)
        return response

    def get_all(self):
        return []


def test_create_interests():
    app.dependency_overrides[InterestsRepository] = InterestsRepositoryMock
    interests = {
        "id": 1,
        "name": "Art",
    }

    response = client.post(
        "/api/interests",
        json.dumps(interests),
    )

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Art"

    app.dependency_overrides = {}


def test_get_all_interests():
    app.dependency_overrides[InterestsRepository] = InterestsRepositoryMock

    response = client.get("/api/interests")

    assert response.status_code == 200
    assert response.json() == []

    app.dependency_overrides = {}
