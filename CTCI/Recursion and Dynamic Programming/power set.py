"""
write a method to return all subsets of a set
"""


def powerSet(sets):
    result = {frozenset()}
    for element in sets:
        addition = set()
        for subset in result:
            addition.add(subset.union(element))
        result = result.union(addition)
    return result
