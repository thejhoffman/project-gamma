from fastapi.testclient import TestClient
from main import app
from queries.occasions import OccasionRepository
import json

client = TestClient(app)

class OccasionRepositoryMock:
    def get_all(self):
        return []

    def create_occasion(self, occasion):
        response = {
            "id": 1,
            "name": "Christmas",
            "date": "2022-12-05"
        }
        response.update(occasion)
        return response

    def get_occasion(self, id):
        response = {
            "id": 1,
            "name": "Christmas",
            "date": "2022-12-25"
        }
        if response.get("id") == id:
            return response

    def update_occasion(self, id, occasion):
        response = {
            "id": 1,
            "name": "string",
        }
        if response.get("id") == id:
            response.update(occasion)
            return response

    def delete_occasion(self, id):
        response = {
            "id": 1,
            "name": "Christmas",
            "date": "2022-12-25"
        }
        if response.get("id") == id:
            response = True
        return response


def test_get_all():
    # Arrange
    app.dependency_overrides[OccasionRepository] = OccasionRepositoryMock

    # Act
    response = client.get('/api/occasions')

    # Assert
    assert response.status_code == 200
    assert response.json() == []

    app.dependency_overrides = {}

def test_create_occasion():
    # Arrange
    app.dependency_overrides[OccasionRepository] = OccasionRepositoryMock
    occasion = {
        "name": "Christmas",
        "date": "2022-12-25"
    }

    # Act
    response = client.post('/api/occasions', json.dumps(occasion))

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Christmas"
    assert response.json()["date"] == "2022-12-25"

    app.dependency_overrides = {}

def test_get_occasion():
    # Arrange
    app.dependency_overrides[OccasionRepository] = OccasionRepositoryMock
    id = 1

    # Act
    response = client.get(f'/api/occasions/{id}')

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Christmas"
    assert response.json()["date"] == "2022-12-25"

    app.dependency_overrides = {}


def test_update_occasion():
    # Arrange
    app.dependency_overrides[OccasionRepository] = OccasionRepositoryMock
    id = 1
    occasion = {
        "name": "Christmassy",
        "date": "2022-12-25"
    }

    # Act
    response = client.put(f"/api/occasions/{id}", json.dumps(occasion))

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Christmassy"
    assert response.json()["date"] == "2022-12-25"

    app.dependency_overrides = {}

def test_delete_occasion():
    # Arrange
    app.dependency_overrides[OccasionRepository] = OccasionRepositoryMock
    id = 1

    # Act
    response = client.delete(f"/api/occasions/{id}")

    # Assert
    assert response.status_code == 200
    assert response.json()

    app.dependency_overrides = {}
