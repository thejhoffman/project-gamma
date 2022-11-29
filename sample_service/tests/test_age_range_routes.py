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
            "id": 1,
            "age": "Test Range",
        }
        response.update(age_range)
        return response


def test_get_all_age_ranges():
    # Arrange
    app.dependency_overrides[AgeRangeQueries] = AgeRangeQueriesMock

    # Act
    response = client.get("/api/age_range")

    # Assert
    assert response.status_code == 200
    # assert response.json() == {"trucks": []}

    # Cleanup
    app.dependency_overrides = {}


def test_create_age_range():
    # Arrange
    app.dependency_overrides[AgeRangeQueries] = AgeRangeQueriesMock
    age_range = {
        "age": "Test Range",
    }

    # Act
    response = client.post(
        "/api/age_range",
        json.dumps(age_range),
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["age"] == "Test Range"
    assert response.json()

    # Cleanup
