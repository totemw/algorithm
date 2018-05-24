"""
Given 0, 1, &, |, ^
Return the number of ways that an expression can be parenthesized and
achieve a given truth value
"""


def CatalanNumber(n):  # (2n)! / (n + 1)!n!
    number = 1
    for i in range(n + 1, 2 * n + 1):
        number *= i
    for i in range(1, n + 2):
        number /= i
    return number


def count_eavl(expr, value, memo=None):
    if len(expr) % 2 == 0:
        return Exception("Stupid expression")
    if len(expr) == 1:
        return int((expr == "0") ^ value)
    if not memo:
        memo = {}
    elif expr in memo:
        counts = memo[expr]
        return counts[int(value)]
    true_count = 0
    for i in range(1, len(expr) - 1, 2):
        left, op, right = expr[:i], expr[i], expr[i + 1:]
        if op == '&':
            true_count += count_eavl(left, True, memo) * count_eavl(right, True, memo)
        elif op == '|':
            true_count += count_eavl(left, True, memo) * count_eavl(right, True, memo)
            true_count += count_eavl(left, False, memo) * count_eavl(right, True, memo)
            true_count += count_eavl(left, True, memo) * count_eavl(right, False, memo)
        elif op == '^':
            true_count += count_eavl(left, True, memo) * count_eavl(right, False, memo)
            true_count += count_eavl(left, False, memo) * count_eavl(right, True, memo)
        else:
            return Exception("you are stupid too")
    total_count = CatalanNumber((len(expr) - 1) / 2)
    false_count = total_count - true_count
    counts = (false_count, true_count)
    memo[expr] = counts
    return counts[int(value)]