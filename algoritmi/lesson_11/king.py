

from loguru import logger


n = 7
m = 5
lst = [[0]*(m) for _ in range(n)]
for i in range(len(lst)):
    for j in range(len(lst[0])):
        up = lst[i-1][j] if i else 0
        left = lst[i][j-1] if j else 0
        lst[i][j] = sum([up, left]) or 1

for i in lst:
    logger.info(i)
