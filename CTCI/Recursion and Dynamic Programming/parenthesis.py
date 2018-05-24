"""
print all valid combinations of n pairs of parentheses
"""


def addParen(array, left, right, s, index):
    if left < 0 or right < left:
        return
    if left == 0 and right == 0:
        array.append("".join(s))
    else:
        s[index] = '('
        addParen(array, left - 1, right, s, index + 1)
        s[index] = ')'
        addParen(array, left, right - 1, s, index + 1)


def generateParens(count):
    s = ["" for _ in range(2 * count)]
    result = []
    addParen(result, count, count, s, 0)
    return result



def parens1(n):
    parens_of_length = [[""]]
    if n == 0:
        return parens_of_length[0]
    for length in xrange(1, n + 1):
        parens_of_length.append([])
        for i in xrange(length):
            for inside in parens_of_length[i]:
                for outside in parens_of_length[length - i - 1]:
                    parens_of_length[length].append("(" + inside + ")" + outside)
    return parens_of_length

print parens1(3)

