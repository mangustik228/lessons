

def evclid(a, b):
    if a == b:
        return a
    if a > b:
        a, b = b, a
    return evclid(a, b-a)
