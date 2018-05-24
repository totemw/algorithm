"""
replace all spaces with %20
"""


def replaceSpace(s, l):
    s = list(s)
    space = 0
    for i in range(l):
        if s[i] == ' ':
            space += 1
    newLength = l + space * 2
    for i in range(l - 1, -1, -1):
        if s[i] == ' ':
            s[newLength - 1] = '0'
            s[newLength - 2] = '2'
            s[newLength - 3] = '%'
            newLength -= 3
        else:
            s[newLength - 1] = s[i]
            newLength -= 1

    return ''.join(s)


a = replaceSpace("asd asfas f    ", 11)
print a

