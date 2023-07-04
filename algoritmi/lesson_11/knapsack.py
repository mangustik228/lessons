from loguru import logger


def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] +
                               dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp


def main():
    weights = [2, 3, 4, 1]  # Вес
    values = [3, 4, 5, 2]  # Стоимость
    capacity = 5
    result = knapsack(weights, values, capacity)
    for i in result:
        logger.info(i)


if __name__ == '__main__':
    main()
