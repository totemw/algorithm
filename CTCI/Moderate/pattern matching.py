"""
you are given two strings, pattern and value. The pattern string consists of
consists of just the letters a and b, describing a pattern within a string

eg. catcatgocatgo matches aabab

Once we pick a, we pick b two, like a = cat, than b must be go
"""



def doesMatch(pattern, value):
    if len(pattern) == 0:
        return len(value) == 0

    mainChar = value[0]
    alterChar = 'a' if mainChar == 'b' else 'b'

    countOfMain = len(filter(lambda x: x == mainChar, value[:]))
    countOfAlter = len(pattern) - countOfMain
    firstAlt = pattern.index(alterChar)
    maxMainSize = len(value) / countOfMain

    for i in range(0, maxMainSize + 1):
        remainingLength = len(value) - i * countOfMain
        first = value[:i]
        if countOfAlter == 0 or remainingLength % countOfAlter == 0:
            altIndex = firstAlt * i
            altSize = 0 if countOfAlter == 0 else remainingLength / countOfAlter
            second = "" if countOfAlter == 0 else value[altIndex : altSize + altIndex]
            cand = ""
            for c in pattern:
                if c == mainChar:
                    cand += first
                else:
                    cand += second
            if cand == value:
                return True
    return False