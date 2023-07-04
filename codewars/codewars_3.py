from collections import Counter
three = {
    1: 1000,
    6: 600,
    5: 500,
    4: 400,
    3: 300,
    2: 200
}

one = {
    1: 100,
    5: 50
}


def score(dice: list[int]):
    c = Counter(dice)
    result = 0
    for i in range(1, 7):
        if c[i] >= 3:
            result += three[i]
            c[i] = c[i] - 3
        result += one.get(i, 0) * c[i]
        c[i] = 0
    return result


score([1, 1, 1, 3, 1])
