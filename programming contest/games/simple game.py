"""
two players take 1 or 3 stones at a time

state x is winning if
- x - 1 is a losing state
- x - 3 is a losing state
- 0 is a losing state

here is a table:
n  0  1  2  3  4  5  6  7
   L  W  L  W  L  W  L  W

if n is odd -> first player wins, else, second one wins

Note: no cycle -> can solve the problem bottom-up (DP)
"""
