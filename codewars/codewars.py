from loguru import logger
import itertools


print(['1', '2'].index('2'))

PANEL = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["", "0", ""]
]


def find_symbol(s: str):
    for i, value in enumerate(PANEL):
        try:
            return i, value.index(s)
        except:
            ...
    raise Exception("no number")


def add_symbol(i: int, j: int, result: set):
    try:
        if i < 0:
            i = 0
        if j < 0:
            j = 0
        if PANEL[i][j]:
            result.add(PANEL[i][j])
    except:
        ...


def get_neigbors_symbols(i: int, j: int):
    result = set()
    add_symbol(i, j, result)
    add_symbol(i-1, j, result)
    add_symbol(i, j-1, result)
    add_symbol(i+1, j, result)
    add_symbol(i, j+1, result)
    return "".join(list(result))


def shuffle_result(list_symbols: list[str]):
    combinations = list(itertools.product(*list_symbols))
    result = []
    for combination in combinations:
        result.append("".join(combination))
    return result


def get_pins(pin: str):
    symbols = []
    for symbol in pin:
        i, j = find_symbol(symbol)
        symbols.append(get_neigbors_symbols(i, j))
    print(symbols)
    result = shuffle_result(symbols)
    return result


def check_result():
    expectations = [('8', ['5', '7', '8', '9', '0']),
                    ('11', ["11", "22", "44", "12",
                     "21", "14", "41", "24", "42"]),
                    ('369', ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398", "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359", "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"])]
    for pin, expect in expectations:
        result = sorted(get_pins(pin))
        logger.info(f'{result = }')
        assert result == sorted(expect)


get_pins("8")
