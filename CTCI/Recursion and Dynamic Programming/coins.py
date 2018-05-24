"""
Given an infinite number of 25cents, 10cents, 5cents and
1 cent, write code to calculate the number of ways of
representing n cents
"""


def coins(cents):
    count = 0
    for i in range(cents, -1, 25):
        count += coins10(i)
    return count


def coins10(cents):
    count = 0
    for i in range(cents, -1, 10):
        count += i / 5 + 1
    return count
