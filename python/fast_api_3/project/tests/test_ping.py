from starlette.testclient import TestClient
import httpx


def test_app(test_app: TestClient):
    response: httpx.Response = test_app.get('/ping')
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "ping": "pong", "debug": True}


def test_get_data(test_app: TestClient):
    response = test_app.get('/data')
    assert response.status_code == 200
    data: dict = response.json()
    assert isinstance(data, dict)
    assert data.get('status') == 'ok'
    assert data.get("sleep") <= 4 or data.get("sleep") >= 0
