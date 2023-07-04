from functools import lru_cache

from loguru import logger


@lru_cache
def livenstein_recursion(A: str, B: str):
    if not A or not B:
        return len(A) + len(B)
    if A[-1] == B[-1]:
        return livenstein_recursion(A[:-1], B[:-1])
    else:
        return 1 + min(
            livenstein_recursion(A[:-1], B[:-1]),
            livenstein_recursion(A[:-1], B),
            livenstein_recursion(A,      B[:-1]),
        )


def livenstein(A: str, B: str):
    F = get_template_table(A, B)
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(
                    F[i-1][j-1],
                    F[i-1][j],
                    F[i][j-1]
                )

    return F[i][j]


def get_template_table(A: str, B: str):
    '''
    # Создаем таблицу формата:
    # [0,1,2,3, ...]
    # [1,0,0,0, ...]
    # [2,0,0,0, ...]
    # ... 
    # Где высота: len(A) + 1
    # Где ширина: len(B) + 1
    # Стоит отметить, что 1,2,3,4 - это крайние случаи(из пустой строки в слово.)
    '''
    F = [[(i+j) if i*j == 0 else 0
         for j in range(len(B) + 1)]
         for i in range(len(A) + 1)]
    return F


def main():
    A = "вор"
    B = "кот"
    result = livenstein_recursion(A, B)
    logger.info(f'{result = }')

    result = livenstein(A, B)
    for i in result:
        logger.info(i)
    logger.info(f'{result = }')


if __name__ == '__main__':
    main()
