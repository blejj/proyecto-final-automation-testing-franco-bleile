from utils.api_client import APIClient


def test_delete_post():

    api = APIClient()

    response = api.delete("/posts/1")

    assert response.status_code == 200