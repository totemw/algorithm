"""
Given a string x = x1-n, find the minimum number
of characters that need to be inserted to make it
a palindrome

Sub problem:
Dij be the minimum numbers of characters that need to be
inserted to make xi-j into a palindrome.

Recurrence:
Dij = - 1 + min{ Di+1,j , Di,j-1 }  (xi != xj)
      - Di+1, j-1 (x1 == xj)

"""


def minPalindrome(s):
    l = len(s)
    dp = [[0 for _ in range(l + 1)] for _ in range(l + 1)]
    for i in range(l, 0, -1):
        for j in range(i + 1, l + 1):
            if s[i - 1] == s[j - 1]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
    return dp[1][-1]


print minPalindrome("Ab3bd")

# MENTION that the order of iteration
