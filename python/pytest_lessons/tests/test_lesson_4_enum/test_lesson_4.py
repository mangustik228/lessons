from tests.src.enums import GlobalErrorMessages


def test_wrong_message():
    assert 200 == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value