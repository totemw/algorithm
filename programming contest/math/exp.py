def power(a, n):
    if not n:
        return 1
    if n == 1:
        return a
    t = a ** (n / 2)
    return t * t * power(a, n % 2)


def Power(a, n):
    result = 1
    while n:
        if n % 2 == 1:
            result *= a
        a *= a
        n /= 2
    return result

