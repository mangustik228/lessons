from loguru import logger


class MyStack(list):
    def push(self, other):
        self.append(other)

    def pop_two_element(self) -> tuple[int, int]:
        b = self.pop()
        a = self.pop()
        return a, b

    def last_element(self):
        return self[-1]

    def add(self):
        a, b = self.pop_two_element()
        self.append(a + b)

    def devision(self):
        a, b = self.pop_two_element()
        self.append(a / b)

    def multiply(self):
        a, b = self.pop_two_element()
        self.append(a * b)

    def minus(self):
        a, b = self.pop_two_element()
        self.append(a - b)

    def calculate(self, el):
        if el == "+":
            self.add()
        elif el == "/":
            self.devision()
        elif el == "*":
            self.multiply()
        elif el == "-":
            self.minus()


def check_brackets(text: str):
    stack = MyStack()
    pairs = {"]": "[", "}": "{", ")": "("}
    for symbol in text:
        if symbol in pairs.values():
            stack.push(symbol)
        if symbol in pairs.keys():
            try:
                if not (stack.pop() == pairs[symbol]):
                    return False
            except IndexError:
                return False

    return not bool(stack)


def checker_func(open_bracket: str, close_bracket: str) -> callable:
    open_bracket = open_bracket
    close_bracket = close_bracket
    count = 0

    def inner_function(symbol: str, check=False):
        nonlocal count
        if check:
            return not bool(count)
        if symbol != open_bracket and symbol != close_bracket:
            return True
        elif symbol == open_bracket:
            count += 1
        elif symbol == close_bracket:
            count -= 1
        return True if count >= 0 else False
    return inner_function


def funny_check(text):
    # Не получилось... (([])) не получаеться без стека сохранить прошлую скобку.
    squad_bracket = checker_func('[', ']')
    round_bracket = checker_func('(', ')')
    figure_bracket = checker_func('{', '}')
    for symbol in text:
        a = squad_bracket(symbol)
        b = round_bracket(symbol)
        c = figure_bracket(symbol)
        if not (a and b and c):
            return False
    return squad_bracket('', check=True) \
        and round_bracket('', check=True)\
        and round_bracket('', check=True)


def main(): ...


if __name__ == '__main__':
    main()
