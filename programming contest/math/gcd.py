def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

# O(log a + b)
