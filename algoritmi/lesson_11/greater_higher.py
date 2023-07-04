import random
from loguru import logger

# My_version


# def greater_higher(A):
#     B = sorted(A)
#     lst = [[0]*(len(B) + 1) for _ in range(len(B) + 1)]
#     for i in range(1, len(A) + 1):
#         for j in range(1, len(B) + 1):
#             if A[i-1] == B[j-1]:
#                 lst[i][j] = 1 + lst[i-1][j-1]
#             else:
#                 lst[i][j] = max(
#                     lst[i][j-1],
#                     lst[i-1][j]
#                 )
#     return lst[-1][-1]

# class Fasade:
#     len_list = 10

#     @classmethod
#     def start_process(cls):
#         while True:
#             A = [random.randint(1, 25) for _ in range(cls.len_list)]
#             result = greater_higher(A)
#             if result[-1][-1] <= 2:
#                 break

#         logger.debug(A)
#         for i in result:
#             logger.debug(i)

# Решения Хирьянова


def greater_higher(A: list):
    F = [0] * (len(A) + 1)
    for i in range(1, len(A)+1):
        m = 0
        for j in range(0, i):
            if A[i-1] > A[j] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F


def main():
    # Fasade.start_process()
    l = greater_higher([1, 3, 2, 4, 2, 5])
    print(l)


if __name__ == '__main__':
    main()
