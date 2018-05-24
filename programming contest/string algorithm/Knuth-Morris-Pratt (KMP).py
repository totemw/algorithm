# coding=utf-8
"""
Knuth-Morris-Pratt (KMP) Matcher

a linear time algorithm - preprocess P in O(len(T)) time
Main idea: skip some comparisons by using the previous result


A[i] is the largest integer smaller than i
such that P1 ... PA[i] is a suffix of P1 ... Pi
A[0] = -1

Intuition: we look at all the prefixes of P that are suffixes of
P1 . . . Pi−1, and find the longest one whose next letter
matches Pi

A[i] = A(k)[i - 1] + 1 where k is the smallest integer
that satisfies P (A(k)[i - 1] + 1) = Pi
(we know that P1..PA[i], P1..PA[A[i]], P1...PA[A[A[i]]] are suffixes of P1...i)

implementation:
A[0] = -1
k = -1
for i in range(1, len(P) + 1):
    while (k >= 0 and P[k + 1] != P[i]):
        k = A[k]
    A[i] = k + 1
    k += 1


Matching:
Loop through T, for any mismatched character,
shift by #matched - A[#matched]

pattern matching implementation:

k = 0
for i in range(1, len(T) + 1):
    while (k >= 0 and P[k + 1] != T[i]):
        k = A[k]
    k += 1
    if (k == len(P)):
    # P matches T[i - m + 1 ... i]
        k = A[k]
"""