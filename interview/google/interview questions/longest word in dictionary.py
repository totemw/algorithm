"""
Longest Word in Dictionary 2
In this problem we will extend Longest Word in Dictionary
     def longestWord(self, words):
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word
by allowing insertion of a new character in
any position not only at the end. Return the construction path of the longest word.
Example 1:

Input: words = ["o", "or", "ord", "word", "world"]
Output: ["o", "or", "ord", "word", "world"]
Example 2:

Input: ["o", "or", "ord", "word", "world", "p", "ap", "ape", "appe", "apple", "apples"]
Output: ["p", "ap", "ape", "appe", "apple", "apples"]
"""
def longestStrChain(words):
    """
    dp: split to level and find path from bottom to top
    keep lenth of 2 level
    f[i + 1] = f[i] + (i if this word can be added a word from previous level)
    """
    s = sorted(words, key=len)
    m = {}
    parent = {}

    for w in s:
        m[w] = 1
        for i in range(len(w)):
            if w[:i] + w[i + 1:] in m:
                # record parent
                m[w] = max(m[w], m[w[:i] + w[i + 1:]] + 1)