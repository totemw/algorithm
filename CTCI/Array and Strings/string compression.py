"""
compress string by counting the repeats
eg. aabcccccaaa -> a2b1c5a3
"""


def compress(s):
    if len(s) == 0:
        return s
    count = 1
    result = ""
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            result += s[i] + str(count)
            count = 1
        else:
            count += 1
    result += s[-1] + str(count)
    return result if len(result) < len(s) else s


