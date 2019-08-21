"""
Given an array nums of length n. All elements appear in pairs except one of them.
Find this single element that appears alone.
Pairs of the same element cannot be adjacent:

[2, 2, 1, 2, 2] // ok
[2, 2, 2, 2, 1] // not allowed
Example 1:
Input: [2, 2, 1, 1, 9, 9, 5, 2, 2]
Output: 5

Example 2:
Input: [1, 1, 2]
Output: 2

Example 3:
Input: [3, 3, 2, 3, 3]
Output: 2
"""

"""
public static int singleElement(int... nums) {
    int lo = 0;
    int hi = nums.length - 1;
    while (lo < hi) {
        int mid = (lo + hi) >>> 1;
        int rightLen = hi - mid + 1;
        
        // odd
        if ((rightLen & 1) == 1) {
            if (nums[mid] == nums[mid + 1]) {
                lo = mid + 2;
            } else {
                hi = mid;
            }
        }
        // even
        else {
            if (nums[mid] == nums[mid + 1]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
    }
    return nums[lo];
}

"""