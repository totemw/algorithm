# Given an input string, reverse the string word by word.

def reverseWords(self, s):
    return " ".join(s.split()[::-1])
