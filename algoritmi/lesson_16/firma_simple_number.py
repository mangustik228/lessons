

# Для любого простого числа p и любого натурального числа где a%p
# a^{p -1} = 1 mod p
def ferma(n: int):
    if n <= 3:
        return True

    for i in range(2, 4):
        if (i ** (n-1)) % n != 1:
            return False
    return True


def check_simple(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


print(pow(5, 2, 3))
print(check_simple(2))
