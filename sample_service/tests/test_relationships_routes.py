from fastapi.testclient import TestClient
from main import app
from queries.relationships import RelationshipRepository
import json

client = TestClient(app)


class RelationshipRepositoryMock:
    def get_all(self):
        return []

    def create_relationship(self, relationship):
        response = {
            "id": 1,
            "type": "Husband"
        }
        response.update(relationship)
        return response

    def get_relationship(self, id):
        response = {
            "id": 1,
            "type": "Husband"
        }
        if response.get("id") == id:
            return response

    def update_relationship(self, id, relationship):
        response = {
            "id": 1,
            "type": "Husband"
        }

        if response.get("id") == id:
            response.update(relationship)
            return response

    def delete_relationship(self, id):
        response = {
            "id": 1,
            "type": "Husband"
        }
        if response.get("id") == id:
            response = True
        return response


def test_get_all():
    # Arrange
    app.dependency_overrides[
        RelationshipRepository
    ] = RelationshipRepositoryMock

    # Act
    response = client.get('/api/relationships')

    # Assert
    assert response.status_code == 200
    assert response.json() == []

    app.dependency_overrides = {}


def test_create_relationship():
    # Arrange
    app.dependency_overrides[
        RelationshipRepository
    ] = RelationshipRepositoryMock
    relationship = {
        "type": "Husband"
    }

    # Act
    response = client.post('/api/relationships', json.dumps(relationship))

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["type"] == "Husband"

    app.dependency_overrides = {}


def test_get_relationship():
    # Arrange
    app.dependency_overrides[
        RelationshipRepository
    ] = RelationshipRepositoryMock
    id = 1

    # Act
    response = client.get(f'/api/relationships/{id}')

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["type"] == "Husband"

    app.dependency_overrides = {}


def test_update_relationship():
    # Arrange
    app.dependency_overrides[
        RelationshipRepository
    ] = RelationshipRepositoryMock
    id = 1
    relationship = {
        "type": "Wife"
    }

    # Act
    response = client.put(f"/api/relationships/{id}", json.dumps(relationship))

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["type"] == "Wife"

    app.dependency_overrides = {}


def test_delete_relationship():
    # Arrange
    app.dependency_overrides[
        RelationshipRepository
    ] = RelationshipRepositoryMock
    id = 1

    # Act
    response = client.delete(f"/api/relationships/{id}")

    # Assert
    assert response.status_code == 200
    assert response.json()

    app.dependency_overrides = {}
