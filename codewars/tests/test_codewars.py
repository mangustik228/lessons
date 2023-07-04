import pytest
from codewars import find_symbol, get_neigbors_symbols, get_pins


PANEL = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["", "0", ""]
]


def test_find_symbol():
    assert find_symbol("5") == (1, 1)


def test_get_neigbors_symbols():
    assert sorted(get_neigbors_symbols(0, 0)) == ["1", "2", "4"]
    assert sorted(get_neigbors_symbols(1, 1)) == [
        "2", "4", "5", "6", "8"]


@pytest.mark.parametrize(
    "pin, result",
    [
        ('8', ['5', '7', '8', '9', '0']),
        ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
        ('369', ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398", "256", "296", "259", "368", "638",
         "396", "238", "356", "659", "639", "666", "359", "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"])
    ]
)
def test_get_pin(pin, result):
    assert sorted(get_pins(pin)) == sorted(result)
