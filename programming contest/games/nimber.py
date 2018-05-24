"""
Grundy Number - Nimber

given heaps of size n1, n2, ... nm
the first player wins iff nim-sum: n1 XOR n2 XOR n3.... is nonzero
0 - lose state

T1, T2 ... reachable from S
g(S) -> smallest nonnegative integer in {g(T1), g(T2), ...}

eg. move 1 or 2:
n    0 1 2 3 4 5 6 7 8
g(n) 0 1 2 0 1 2 0 1 2
"""