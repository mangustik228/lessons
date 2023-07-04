from loguru import logger


A = [*range(5)]
B = [1, 10, 11,  12, 2, 1, 2, 3, 6,  8, 9]


def greater_common(A: list, B: list):
    F = [[0]*(len(B)+1) for _ in range(len(A)+1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(
                    F[i-1][j],
                    F[i][j-1])
    return F


def main():
    result = greater_common(A, B)
    logger.info(f"{A = }")
    logger.info(f"{B = }")
    for i in result:
        logger.info(i)


if __name__ == '__main__':
    main()
