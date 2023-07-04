from loguru import logger

# Бинарный поиск в массиве (отсортированном)


def binary_search(lst: list, search: int):
    left = -1
    right = len(lst)
    while right-left > 1:
        middle = (left + right) // 2
        if search < lst[middle]:
            right = middle
        else:  # search >= lst[middle]
            left = middle
    return middle


def main():
    r = binary_search([1, 7], 3)
    logger.info(f'{r}')


if __name__ == '__main__':
    main()
