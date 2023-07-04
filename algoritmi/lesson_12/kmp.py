from loguru import logger

# TODO


def create_pi(pattern):
    T = pattern
    pi = [0] * len(pattern)
    j = 0
    for i in range(len(pi)):
        if T[j] == T[i]:
            j += 1
            pi[i] = ...


def main():
    logger.debug(f'start')
    pattern = 'лилила'
    text = "Привет мир. лилилф очень хочет быть лилилилилилилила"
    pi = create_pi(pattern)


if __name__ == '__main__':
    main()
