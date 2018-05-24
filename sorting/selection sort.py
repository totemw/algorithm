#time: O(n^2)
#space:

def selectionSort(alist):
    for i in range(len(alist)):
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist