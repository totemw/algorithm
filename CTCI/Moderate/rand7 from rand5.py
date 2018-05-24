"""
Given rand5(), generates rand7()
"""
import random


def rand5():
    return random.randint(0, 5)


def rand7():
    num = 5 * rand5() + rand5() # each value is equally possible
    if num < 21:
        return num % 21