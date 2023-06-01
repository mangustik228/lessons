from utils import read_from_file
import pytest
from .conftest import test_data, fp


def create_test_data(test_data):
    with open(fp, 'w') as file: 
        file.writelines(test_data)


def test_read_from_file_1():
    create_test_data(test_data)
    assert test_data == read_from_file(fp)


def test_read_from_file_2():
    test_data = ['one\n','three\n','four\n','five\n']
    create_test_data(test_data)
    assert test_data == read_from_file(fp)


def test_read_from_file_3():
    test_data = ['one\n','three\n','four\n','five\n', 'second\n']
    create_test_data(test_data)
    assert test_data == read_from_file(fp)