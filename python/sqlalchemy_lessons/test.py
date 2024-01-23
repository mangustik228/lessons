

txt = "This is text for task: reverse every word in sentence"


def reverse_txt(txt: str) -> str:
    ...
    result = ""
    last_symbol_is_letter = False
    for letter in txt:
        if letter.isalpha() and not last_symbol_is_letter:
            word = letter
            last_symbol_is_letter = True
        elif letter.isalpha() and last_symbol_is_letter:
            word += letter
        elif not letter.isalpha():
            if last_symbol_is_letter:
                result += word[::-1]
                last_symbol_is_letter = False
            result += letter
    if word:
        result += word[::-1]

    return result


def main():
    assert (r := reverse_txt("This is text for")) == "sihT si txet rof", r
    print(reverse_txt(txt))
    hello = "this is just text"
    print(f"{hello!r}")


if __name__ == '__main__':
    main()
