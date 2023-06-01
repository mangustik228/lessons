import pytest

fp = "./testfile.txt"
test_data = ["one\n", "two\n", "three\n"]

@pytest.fixture(autouse=True)
def clean_text_file():
    with open(fp, 'w'):
        ...

