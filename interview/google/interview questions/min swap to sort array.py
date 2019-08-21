"""
Given an array return an integer indicating the minimum number
of swap operations required to sort the array into ascending order.

Example 1:

Input: [5, 1, 3, 2]
Output: 2
Explanation: [5, 1, 3, 2] -> [2, 1, 3, 5] -> [1, 2, 3, 5]
Example 2:

Input: [1, 3, 2]
Output: 1
Explanation: [1, 3, 2] -> [1, 2, 3]

visualizing as graph
find cycles: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
"""

def minSwaps(arr):
    n = len(arr)

    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]

    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    arrpos.sort(key=lambda it: it[1])

    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):

        # alreadt swapped or
        # alreadt present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue

        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1

        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
            # return answer
    return ans


# Driver Code
arr = [1, 5, 4, 3, 2]
print(minSwaps(arr))

def selectionSort(alist):
    for i in range(len(alist)):
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist