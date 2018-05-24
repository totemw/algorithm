"""
check whether two strings are one edit away: insert, remove, replace
"""

# subproblem s1[:i], s2[:j]

def oneEditAway(s1, s2):
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(len(s2) + 1):
        dp[0][i] = i
    for i in range(len(s1) + 1):
        dp[i][0] = i
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + 0 if s1[i - 1] == s2[j - 1] else 1)
    return dp[-1][-1] < 2


def OneEditAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) > len(s2):
        s1, s2 = s2, s1 # s2 >= s1
    index1 = 0
    index2 = 0
    check = False
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if check:
                return False
            check = True
            if len(s1) == len(s2):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True



