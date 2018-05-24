#time O(nlogn)

class Sort:
    def mergeSort (self, alist):
        if len(alist) <= 1:
            return alist
        mid = len(alist) / 2
        left = self.mergeSort(alist[:mid])
        right = self.mergeSort(alist[mid:])
        return self.mergeSortArray(left, right)

    #return a new sorted array
    def mergeSortArray(self, l1, l2):
        result = []
        l = 0
        r = 0
        while l < len(l1) and r < len(l2):
            if l1[l] < l2[r]:
                result.append(l1[l])
                l += 1
            else:
                result.append(l2[r])
                r += 1
        result += l1[l:]
        result += l2[r:]
        return result