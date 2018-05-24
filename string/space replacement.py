"""
Write a method to replace all spaces in a string with %20.
The string is given in a characters array, you can assume it has enough space
for replacement and you are given the true length of the string.
"""
# time: O(n) space: O(1)
class solution:
    # s is a char[]
    def replaceBlank(self, s, length):
        if s is None:
            return length
        spaces = 0
        for c in s:
            if c == ' ':
                spaces += 1
        l = length + spaces * 2
        index = l - 1
        for i in range(length - 1, -1, -1):
            if s[i] == ' ':
                s[index] = '0'
                s[index - 1] = '2'
                s[index - 2] = '%'
                index -= 3
            else:
                s[index] = s[i]
                index -= 1
        return l
