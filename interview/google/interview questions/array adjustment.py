"""
Given an integer array nums containing positive elements and an int maxValue.
Find the value of x such that the sum of the elements of the array
is maximum and is less than the given maxValue.
x is defined as: if the current value is greater than x,
then x is used as the new value, otherwise keep the original value nums[i] = min(x, nums[i]).

Example 1:

Input: nums = [10, 5, 20, 30], maxValue = 40
Output: 12
Explanation:
If x = 10, the array would be nums = [10, 5, 10, 10] and the sum of the array elements would be 35.
If x = 12, the array would be nums = [10, 5, 12, 12] and the sum of the elements would be 39 which is the maximum sum close to given maxValue which is 40.
So the answer would be 12.
"""

def budgetize(sals, budget):
    i = len(sals) - 1
    count = 1 # counts how many high salaries we are converting to k
    while i >= 0:
        # sort salaries so you can cherrypick highest sals and start replacing them with k
        sorted_sals = sorted(sals)
        # find the sum of all the salaries except the highest one(s)
        # as i decreases, this array will reduce in size i.e. we will exclude highest and second highest sal in
        # next iteration, then highest , second highest and third highest in next and so on..
        sum_of_sals_excluding_highest = sum(sorted_sals[:i])
        # find k by substracting this sum from the budget..
        k = (budget - sum_of_sals_excluding_highest)/count
        if max(sorted_sals[:i]) > k: # this means there are still salries higher than k...
            i -= 1 # reduce i to now convert the next highest salary..
            count += 1 # increase by one since now another high salary will be converted to k..
        else:
            return k
