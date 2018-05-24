"""
compute all permutations of a string whose characters are
not necessarily unique
"""

def permutations(s):
    h = {}
    for i in s:
        if i not in h:
            h[i] = 1
        else:
            h[i] += 1
    return permHelper(h)


def permHelper(table):
    k = table.keys()
    if len(k) == 1 and table[k[0]] == 1:
        return [k[0]]

    if table[k[0]] == 1:
        del table[k[0]]
    else:
        table[k[0]] -= 1
    permutation = permHelper(table)
    result = []
    for i, word in enumerate(permutation):
        for j in range(len(word) + 1):
            tmp = word[:j] + k[0] + word[j:]
            if tmp not in result:
                result.append(tmp)
    return result


print permutations("aaB")


def permutations(string):
    return partial_permutations("", sorted(string))


def partial_permutations(partial, letters):
    if len(letters) == 0:
        return [partial]
    permutations = []
    previous_letter = None
    for i, letter in enumerate(letters):
        if letter == previous_letter:
            continue
        next_partial = partial + letter
        next_letters = letters[:i] + letters[(i+1):]
        permutations += partial_permutations(next_partial, next_letters)
        previous_letter = letter
    return permutations