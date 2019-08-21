"""
https://github.com/python/cpython/blob/master/Lib/bisect.py
"""
"""
first element which >= target
search range: [left, right]
lower_bound(arr, 0, len(arr) - 1, target) find x >= target

eg. a = [1,1,3,5,5,6,6,6,8,9] lower_bound(a,0,len(a) - 1, 4) = 3
"""
def lower_bound(arr, left, right, target):
  while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
      left = mid + 1
    else:
      right = mid
  return left

"""
last element which <= target
search range: (left, right]
upper_bound(arr, -1 , len(arr), target) find x <= target

eg. a = [1,1,3,5,5,6,6,6,8,9] upper_bound(a,-1,len(a), 4) = 2
"""
def upper_bound(arr, left, right, target):
  while left < right:
    mid = (left + right) // 2
    if arr[mid] <= target:
      left = mid + 1
    else:
      right = mid
  return left - 1

"""
lc34  Find First and Last Position of Element in Sorted Array
"""
def searchRange(self, nums, target):
    if not nums:
        return [-1, -1]

    def lower_bound(arr, left, right, target):
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def upper_bound(arr, left, right, target):
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left - 1

    l = lower_bound(nums, 0, len(nums) - 1, target)
    r = upper_bound(nums, -1, len(nums), target)
    print(l)
    print(r)
    if nums[l] != target or nums[r] != target:
        return [-1, -1]

    return [l, r]

def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo

def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid