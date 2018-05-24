"""
easy adn powerful hash function is a polynomial mod some prime p:
- Consider each letter as a number (ASCII value is fine)
- H(x1 ... xk) = x1 a^(k - 1) + x2 a^(k - 2) + ... +xk-1 a + xk (mod p)

Main Idea:
1. pre-process T to speed up queries
    - Hash every substring of length k
    - k is a small constant
2. For each query P, hash the first k letters of P to retrieve
  all the occurrences of it within T.

pros:
easy to inplement
speed up
cons:
O(mn) for terrible hashing
lots of memory consumption
"""