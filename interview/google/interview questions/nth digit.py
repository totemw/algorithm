"""
I had this question awhile back for a Google phone screen.

https://leetcode.com/problems/nth-digit
Basically it was to write a function that returned a specific value at an index
if the array/list only had single digit values for continuous numbers.
Basically the list would look like digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3...]
As you can see after nine, ten is split up into 1 and then 0,
and eleven is split up into 1 and then 1 and etc.
Basically the function was if given an index, return that value at that index.
So function(10) would return 1, function(11) would return 0, function(12) would return 1 and etc.
So at any given index there is only a single digit value.
That means that 100 would be brokent into 1, 0, 0 and 1250 would be 1, 2, 5, 0 and so on and so forth.
"""


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        # find the size of the digit it will be a part of
        i = 1  # digit size
        while (n - i * 9 * (10 ** (i - 1))) > 0:
            n -= i * 9 * (10 ** (i - 1))
            i += 1

        # n digits within the start of the i digit range
        # x = number we want
        # y index within number
        x = 10 ** (i - 1) + (int((n - 1) / (i)))
        y = (n - 1) % (i)

        return int(str(x)[y])