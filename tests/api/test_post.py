from utils.api_client import APIClient

def test_create_post():

    api = APIClient()

    payload = {
        "title": "automation test",
        "body": "hello world",
        "userId": 1
    }

    response = api.post("/posts", payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "automation test"
    assert data["body"] == "hello world"
    assert "id" in data