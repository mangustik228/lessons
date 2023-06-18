import json
from starlette.testclient import TestClient


def test_create_summary(test_app_with_db: TestClient):
    response = test_app_with_db.post(
        "/summaries/",
        content=json.dumps({"url": "https://foo.bar"}))
    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_create_summaries_invalid_json(test_app: TestClient):
    response = test_app.post(
        "/summaries/",
        content=json.dumps({})
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_create_summaries_empty_json(test_app: TestClient):
    response = test_app.post(
        '/summaries/'
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_read_summary(test_app_with_db: TestClient):
    response = test_app_with_db.post(
        "/summaries/",
        content=json.dumps({"url": "https://foo.bar"})
    )
    summary_id = response.json()['id']
    response = test_app_with_db.get(f"/summaries/{summary_id}/")

    response_dict: dict = response.json()

    assert isinstance(response_dict, dict)
    assert response_dict.get("id") == summary_id
    assert response_dict.get("url") == "https://foo.bar"
    assert response_dict.get("summary")
    assert response_dict.get("created_at")


def test_read_summary_incorrect_id(test_app_with_db: TestClient):
    response = test_app_with_db.get('/summaries/99999999/')
    assert response.status_code == 404
    assert response.json()['detail'] == "Summary not found"


def test_get_all_summaries(test_app_with_db: TestClient):
    response = test_app_with_db.post(
        "/summaries/",
        content=json.dumps({"url": "https//foo.bar"}))
    summary_id = response.json()["id"]

    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200

    response_list = response.json()
    assert isinstance(response_list, list)

    def find_element_by_id(val: dict):
        assert isinstance(val, dict)
        assert val.get("id"), "В каком то элементе нет id"
        return val.get("id") == summary_id

    assert [*filter(find_element_by_id, response_list)].__len__() == 1
