import pytest
from lesson_13.structures import check_brackets, funny_check


@pytest.mark.parametrize(
    "text, result",
    [
        ("(hello {world})", True),
        ("([(this) is (text) with {many}] brackets {[!]})", True),
        ("(This is [text with unccorrect){positions]}", False),
        ("This( uncorrect count symbols", False),
        ("Correct count )but( not uncorrect place", False)
    ]
)
def test_funny_brackets_correct(text, result):
    assert funny_check(text) == result


@pytest.mark.parametrize(
    "text, result",
    [
        ("(hello {world})", True),
        ("([(this) is (text) with {many}] brackets {[!]})", True),
        ("(This is [text with unccorrect){positions]}", False),
        ("This( uncorrect count symbols", False),
        ("Correct count )but( not uncorrect place", False)
    ]
)
def test_brackets_correct(text, result):
    assert check_brackets(text) == result
