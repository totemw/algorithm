"""
Given a sorted array of strings that is interspersed with
empty strings, find the location of a given string

eg. ["at", "", "", "ball", "", "", "", "dad"]

again, binary search, find non-empty string as string
"""


def search(strings, s, first, last):
    if first > last:
        return -1
    mid = (first + last) / 2

    if strings[mid] == "":
        left = mid - 1
        right = mid + 1
        while True:
            if left < first and right > last:
                return -1
            elif right <= last and strings[right] != "":
                mid = right
                break
            elif left >= first and strings[left] != "":
                mid = left
                break
            right += 1
            left -= 1
    if strings[mid] == s:
        return mid
    elif strings[mid] < s:
        return search(strings, s, mid + 1, last)
    else:
        return search(strings, s, first, mid - 1)

