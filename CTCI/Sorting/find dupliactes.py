"""
You have an array with all numbers from 1 to N (N <= 32000)
The array may have duplicate entries you do not know what N is
memory: 4 kb
print all duplicates

can create a bitVector with 32000 bits
"""


class BitSet:

    def __init__(self, size):
        self.bitset = list((size >> 5) + 1)  # divide by 32

    def get(self, pos):
        wordNumber = pos >> 5
        bitNumber = pos & 0x1F
        return (self.bitset[wordNumber] & (1 << bitNumber)) != 0

    def set(self, pos):
        wordNumber = pos >> 5
        bitNumber = pos & 0x1F
        self.bitset[wordNumber] |= 1 << bitNumber


def checkDuplicates(array):
    bs = BitSet(32000)
    for i in range(len(array)):
        num = array[i]
        num0 = num - 1 # number starts at 1
        if bs.get(num0):
            print num
        else:
            bs.set(num0)