"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
 is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
"""

# stack

class Solution:

    def decodeString(self, s):
        stack = [["", 1]]
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            elif c == '[':
                stack.append(["", num])
                num = 0
            elif c == ']':
                letter, n = stack.pop()
                stack[-1][0] += letter * n
            else:
                stack[-1][0] += c

        return stack[0][0]





