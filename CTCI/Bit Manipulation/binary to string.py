"""
Given a real number between 0 and 1 that is passed in as a double
print the binary representation
else print ERROR
"""


def printBinary(num):
    if num == 1:
        return "1.0"
    if num == 0:
        return "0.0"
    if num >= 1 or num <= 0:
        return "ERROR"
    binary = ["0."]
    while num > 0:
        if len(binary) >= 32:
            break
        double = num * 2
        if double >= 1:
            binary.append("1")
            num = double - 1
        else:
            binary.append("0")
            num = double
    return "".join(binary)


print printBinary(0.625)