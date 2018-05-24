#time: O(n^2)
#space: O(1)

def bubbleSort (alist):
    for i in range(len(alist)):
        for j in range(1, len(alist) - i):
            if alist[j - 1] > alist[j]:
                alist[j - 1], alist[j] = alist[j], alist[j - 1]
    return alist