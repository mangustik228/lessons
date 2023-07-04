

from loguru import logger


def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k-1]
        if pattern[k] == pattern[i]:
            k += 1
        pi[i] = k
    return pi


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    matches = []

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = pi[q - 1]
    return matches


def main():
    text = "this is text helloh world hello"
    pattern = "helloh"
    result = compute_prefix_function(pattern)
    logger.debug(result)
    result = kmp_search(text, pattern)
    logger.debug(result)


if __name__ == '__main__':
    main()
