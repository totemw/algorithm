"""
Implement a method that sort words,
but instead of using the normal alphabet a, b, c, ..., x, y, z,
we have ch that goes between h and i in the sort order.
So the alphabet becomes a, b, ... h, ch, i, ... x, y, z.

Example 1:

Inout: ["indigo", "charisma", "hotel"]
Output: ["hotel", "charisma", "indigo"]

define a customized key function to transfer the string to a
list of number and sort based on the function:
"""

def chCompare(s):
    def custom_int(word):
        m = len(word)
        out = []
        for i in range(m):
            if i < m - 2 and word[i] == 'c' and word[i + 1] == 'h':
                out.append((ord('h') - ord('a') + 1))
            elif i > 0 and word[i] == 'h' and word[i - 1] == 'c':
                continue
            else:

                tmp = ord(word[i]) - ord('a')
                if tmp <= ord('h') - ord('a'):
                    out.append(tmp)
                else:
                    out.append(tmp + 1)

        return out
    s.sort(key=lambda x: custom_int(x))
    return s