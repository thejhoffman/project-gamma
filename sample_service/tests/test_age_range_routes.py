from fastapi.testclient import TestClient
from main import app
from routers.age_range import AgeRangeQueries
import json

client = TestClient(app)


class AgeRangeQueriesMock:
    def get_all(self):
        return []

    def create(self, age_range):
        response = {
            "id": 0,
            "age": "string",
        }
        response.update({"id": 1})
        response.update(age_range)
        return response

    def get_one(self, id):
        response = {
            "id": 1,
            "age": "Adults (25-64)",
        }
        if response.get("id") == id:
            return response

    def update(self, id, age_range):
        response = {
            "id": 1,
            "age": "string",
        }
        if response.get("id") == id:
            response.update(age_range)
            return response

    def delete(self, id):
        response = {
            "id": 1,
            "age": "string",
        }
        if response.get("id") == id:
            response = True
        return response


def test_get_all_age_ranges():
    # Arrange
    app.dependency_overrides[AgeRangeQueries] = AgeRangeQueriesMock

    # Act
    response = client.get("/api/age_range")

    # Assert
    assert response.status_code == 200
    assert response.json() == []

    # Cleanup
    app.dependency_overrides = {}


def test_create_age_range():
    # Arrange
    app.dependency_overrides[AgeRangeQueries] = AgeRangeQueriesMock
    age_range = {
        "age": "Adults (25-64)",
    }

    # Act
    response = client.post(
        "/api/age_range",
        json.dumps(age_range),
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["age"] == "Adults (25-64)"

    # Cleanup
    app.dependency_overrides = {}


def test_get_one_age_range():
    # Arrange
    app.dependency_overrides[AgeRangeQueries] = AgeRangeQueriesMock
    id = 1

    # Act
    response = client.get(
        f"/api/age_range/{id}",
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["age"] == "Adults (25-64)"

    # Cleanup
    app.dependency_overrides = {}


def test_update_age_range():
    # Arrange
    app.dependency_overrides[AgeRangeQueries] = AgeRangeQueriesMock
    id = 1
    age_range = {
        "age": "Adults (25-64)",
    }

    # Act
    response = client.put(
        f"/api/age_range/{id}",
        json.dumps(age_range),
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["age"] == "Adults (25-64)"

    # Cleanup
    app.dependency_overrides = {}


def test_delete_age_range():
    # Arrange
    app.dependency_overrides[AgeRangeQueries] = AgeRangeQueriesMock
    id = 1

    # Act
    response = client.delete(
        f"/api/age_range/{id}",
    )

    # Assert
    assert response.status_code == 200
    assert response.json()

    # Cleanup
    app.dependency_overrides = {}
