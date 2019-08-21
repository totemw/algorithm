#time: O(nlogn) - O(n ^ 2)

#extra space cost
def quickSort1(alist):
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        return quickSort1([x for x in alist[1:] if x < pivot]) + \
            [pivot] + \
            quickSort1([x for x in alist[1:] if x >= pivot])

#inplace
def quickSort2(alist, start, end):
    if start >= end:
        return
    tmp = start
    for i in range(start + 1, end + 1):
        if alist[i] < alist[start]:
            tmp += 1
            alist[tmp], alist[i] = alist[i], alist[tmp]
    alist[tmp], alist[start] = alist[start], alist[tmp]
    quickSort2(alist, start, tmp - 1)
    quickSort2(alist, tmp + 1, end)

#two-way partition
def quickSort (alist, lower, upper):
    if lower >= upper:
        return
    pivot = alist[lower]
    left, right = lower + 1, upper
    while left <= right:
        while left <= right and alist[left] < pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if left > right:
            break
        alist[left], alist[right] = alist[right], alist[left]
    alist[lower], alist[right] = alist[right], alist[lower]
    quickSort(alist, lower, right - 1)
    quickSort(alist, right + 1, upper)
