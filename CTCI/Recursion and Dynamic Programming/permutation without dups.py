"""
list all permutations of a string that contains
no duplicate letters
"""


def permutations(s):
    if len(s) == 1:
        return [s]
    permutation = permutations(s[:-1])
    result = []
    for i, word in enumerate(permutation):
        for j in range(len(s)):
            tmp = word[:j] + s[-1] + word[j:]
            result.append(tmp)
    return result


print (permutations("abcdefg"))