"""
Given an int array log of length n. Implement the following method

public class Solution {

	public Solution(int[] log) {
		// preprocess
	}

	/**
	*  Returns true if the "logType" appears more than half times in the interval [start, end], otherwise false.
	*/
	public boolean isMoreThanHalf(int start, int end, int logType) {
	}
}

Example:
Solution s = new Solution([6, 6, 6, 7, 3, 8]);
s.isMoreThanHalf(0, 3, 6); // true
s.isMoreThanHalf(1, 4, 6); // false
s.isMoreThanHalf(2, 5, 7); // false

Sol1: O(logn) Solution

Construct segment trees for each logType.
Get the count from the segment tree between i and j in O(log(n) )time.
(count > (j-i+1)/2) return true or false

Sol2: O(1) Solution On2 space

Construct hashMap, store array index as key and value as counts of all logTypes until that point.
From hashMap we can easily get the logType count in O(1) time
(count > (j-i+1)/2) return true or false
"""