"""
When people send messages on their phones they sometimes modify word
spelling by adding extra letters for emphasis.
For example, if you want to emphasize hello you might write it
hellloooooooo. Let's call the ls and the os word extensions.
Regular text contains 2 or fewer of the same character in a row,
 while word extensions have 3 or more of the same character in a row.
 Given an input string representing one word, write a method that returns the start and end indices of all extensions in the word.
https://leetcode.com/problems/positions-of-large-groups


// In JavaScript
function spellCheck(input) {
  const it = getWordExtensions(input, 3);
  for(const x of it) {
    console.dir(x);
  }
}

function* getWordExtensions(input, k) {
  let we, lo, hi;
  for(let i = 0; i < input.length; i ++) {
    const c = input[i];
    if(we === c) {
      hi = i;
    }else{
      // Meet a new char
      if(hi - lo >= k - 1) {
        yield [lo, hi];
      }
      we = c;
      lo = hi = i;
    }
  }

  // Draining
  if(hi - lo >= k - 1) {
    yield [lo, hi];
  }
}

spellCheck('whaaaaatttsup');
/*
[ 2, 6 ]
[ 7, 9 ]
*/

spellCheck('hellloooooooo');
/*
[ 2, 4 ]
[ 5, 12 ]
*/
"""
def repeating_character(s, k):
    if len(s) <= 1:
      return []
    r = [0]
    for i in range(1, len(s)):
      if s[i] != s[i-1]:
        r.append(i)

    result = []
    for i in range(1, len(r)):
      if r[i] - r[i-1] >= k:
        result.append((r[i-1], r[i]))

    if len(s) - r[-1] >= k:
      result.append((r[-1], len(s)))
    return result


import collections
def repeating_character(s):
    d = collections.Counter(s)
    r = []
    for k, v in d.items():
        if v > 1:
            r.append([k, v])
    return r
"""
follow up: 809
Now we want to spell-check extended words. You are given a dictionary of words.
Implement method isExtendedDictionaryWord that will return:
true if it is a dictionary word.
true if you collapse the extensions in the word and it is a dictionary word.
false otherwise.

    def expressiveWords(self, S, words):
        return sum(self.check(S, W) for W in words)

    def check(self, S, W):
        i, j, n, m = 0, 0, len(S), len(W)
        for i in range(n):
            if j < m and S[i] == W[j]: j += 1
            elif S[i - 1:i + 2] != S[i] * 3 != S[i - 2:i + 1]: return False
        return j == m
"""