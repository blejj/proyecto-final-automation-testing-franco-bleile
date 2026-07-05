from utils.api_client import APIClient


def test_get_post():

    api = APIClient()

    response = api.get("/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert "userId" in data
    assert "id" in data
    assert "title" in data