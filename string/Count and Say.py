"""
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.

11 is read off as "two 1s" or 21.

21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.
"""

class Solution:
    def count(self, s):
        result = ''
        count = 0
        current = '#'
        for i in s:
            if i != current:
                if current != '#':
                    result += str(count) + current
                current = i
                count = 1
            else:
                count += 1
        result += str(count) + current
        return result

    def countAndSay(self, n):
        s = '1'
        for i in range(n - 1):
            s = self.count(s)
        return s
