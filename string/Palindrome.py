# Given a string, determine if it is a palindrome
# considering only alphanumeric characters and ignoring cases.

def isPalindrome(self, s):
    if not s:
        return True
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
        return False


