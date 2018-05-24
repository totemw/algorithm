"""
merge sort, given A with extra space
"""


def merge(a, b, lastA, lastB):
    indexA = lastA - 1
    indexB = lastB - 1
    indexMerged = lastA + lastB - 1

    while indexB >= 0:
        if indexA >= 0 and a[indexA] > b[indexB]:
            a[indexMerged] = a[indexA]
            indexA -= 1
        else:
            a[indexMerged] = b[indexB]
            indexB -= 1
        indexMerged -= 1

