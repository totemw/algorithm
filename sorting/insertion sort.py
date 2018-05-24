#time: O(n ^ 2)

def insertionSort (alist):
    for i, item_i in enumerate(alist):
        index = i
        while index > 0 and alist[index - 1] > item_i:
            alist[index] = alist[index - 1]
            index -= 1
        alist[index] = item_i
    return alist