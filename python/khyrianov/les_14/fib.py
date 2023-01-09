def fibonacci(n):
    '''function to find fibonacci variable

    Args:
        n (int): int

    Returns:
        int: fibonacci numbers
    '''
    if not isinstance(n, int):
        raise TypeError("Fibonacci can't work with your type")
    if n < 0:
        raise ValueError("Fibonacci can't work with nehative values")
    if n > 10000:
        raise ValueError("it's very big number. Fibonacci can take numbers less 9999")
        
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def main():
    n = int(input('введите номер числа фибоначчи: '))
    print('ваше число фибоначи: ', fibonacci(n))
    
if __name__ == '__main__':
    main()