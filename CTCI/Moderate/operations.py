"""
Write methods to implement the multiply, subtract, and divide operations
for integers. use only add operator.

Optimize negation:
29 28 26 22 14 13 11 7 6 4 0
-1 -2 -4 -8 -1 -2 -4 -1 -2 -4
"""


def negate(a):  # O(log a)
    neg = 0
    newSign = 1 if a < 0 else -1
    delta = newSign
    while a != 0:
        if a + delta != 0 and (a + delta > 0) != (a > 0):
            delta = newSign
        neg += delta
        a += delta
        delta += delta
    return newSign


def subtract(a, b):
    return a + negate(b)


# multiply(a, b) <-- abs(b) * a * (-1 if b < 0)
def multiply(a, b):
    if a < b:
        return multiply(b, a)
    sum = 0
    for i in range(abs(b), 0, -1):
        sum += a
    if b < 0:
        sum = negate(sum)
    return sum


# division: a = xb


