'''
Пример принципа round-robbin
'''


def gen_1(s):
    for i in s:
        yield i


def gen_2(n):
    for i in range(n):
        yield str(i)


g1 = gen_1("vasiliy")
g2 = gen_2(7)

tasks = [g1, g2]


while tasks:
    task = tasks.pop(0)

    try:
        result = next(task)
        print(result)
        tasks.append(task)
    except StopIteration:
        pass
