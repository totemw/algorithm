"""
Given two 32-bits numbers, N and M, and two bit positions i and j
insert M into N such that M starts at bit j and ends at bit i
"""


# clear i- j  in N, shift M, merge N and M
def updateBits(n, m, i, j):
    # create a mask: 11100011
    allOnes = ~0
    left = allOnes << (j + 1)
    right = (1 << i) - 1
    mask = left | right
    n_cleared = n & mask

    m_shift = m << i
    return n_cleared | m_shift