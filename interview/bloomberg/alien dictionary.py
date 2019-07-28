"""
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
ou receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
"""

"""
chars = set(all words) : w f e t r
1. (wrt, wrf) (wrf, er) (er, ett) (ett, rftt)
2. tf, we, rt, er
3 know words will follow others: f e t r => w is first
4 eliminate all pairs with w: tf rt er
5 know words will follow others: f t r => w->e
6 eliminate all pairs with e: tf rt 
7 know words will follow others: f t  => w->e->r
...

"""

def alienOrder(self, words):
    less = []
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                less += a + b,
                break
    chars = set(''.join(words))
    order = []
    while less:
        free = chars - set(zip(*less)[1])
        if not free:
            return ''
        order += free
        less = filter(free.isdisjoint, less)
        chars -= free
    return ''.join(order + list(chars))