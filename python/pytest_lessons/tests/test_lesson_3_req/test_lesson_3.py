import pytest
import responses
from utils import SomeResourceClient
from main import url,user_id
from datetime import datetime
from requests.exceptions import HTTPError

@responses.activate
def test_some_web_client():
    valid_json_answer = {
        "lastActionTime": 1626615588,
        "timeDiff": 16983
    }
    responses.add(
        method=responses.GET, 
        url=f"https://www.avito.ru/web/user/get-status/{user_id}",
        json=valid_json_answer,
        status=200
    )
    some_resouce_client = SomeResourceClient(url)
    result = some_resouce_client.user_get_last_action_time(user_id)
    assert result == datetime.fromtimestamp(16983)


@responses.activate
def test_some_web_client_error():
    responses.add(
        method=responses.GET,
        url=f"https://www.avito.ru/web/user/get-status/{user_id}",
        status=404
    )

    with pytest.raises(HTTPError):
        some_resource_client = SomeResourceClient(url)
        some_resource_client.user_get_last_action_time(user_id)
