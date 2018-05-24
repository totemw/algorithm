"""
write a method to sort an array of strings so that all the
anagrams are next to each other
"""


def groupAnagrams(strings):
    sortedSting = [sorted(s) for s in strings]
    table = {}
    for s in sortedSting:
        if s in table:
            table[s] += 1
        else:
            table[s] = 0
    result = []
    for key in table.keys():
        result.extend([key] * table[key])
    return result