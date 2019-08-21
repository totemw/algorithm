"""
sliding window template
https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235002/One-code-template-to-solve-all-of-these-problems!
"""
def template(s, t):
    result = []
    if len(t)  > len(s):
        return result
    # hash map to store char count
    m = {}
    for c in t:
        m[c] = m.get(c, 0) + 1
    # count to check whether match the target
    count = len(m)
    # 2 pointers: begin and end
    begin = end = 0
    # loop at the beginning of string
    while end < len(s):
        # get a new char
        c = s[end]
        if c in m:
            m[c] -= 1
            # modify count based on requirement
            if m[c] == 0:
                count -= 1
        end += 1

        # increase begin to make it valid/invalid
        while count == 0:
            c = s[begin]
            if c in m:
                m[c] += 1
                if m[c] > 0:
                    count += 1
        begin += 1
        #save result

    return result

"""
76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""

def minWindow(s, t):
    if len(t) > len(s):
        return ""
    # for key and value in m: if value == 0, means exact match
    m = {}
    for c in t:
        m[c] = m.get(c, 0) + 1

    count = len(m)
    begin = end = 0
    result_start = 0
    result_len = float('inf')

    while end < len(s):
        c = s[end]
        if c in m:
            m[c] -= 1
            if m[c] == 0:
                count -= 1
        end += 1

        while count == 0: # count = 0 means window is valid, we move start until window is invalid
            c = s[begin]
            if c in m:
                m[c] += 1
                if m[c] > 0:
                    count += 1
            # cuz is valid -> invalid, we need to record then update begin
            if end - begin < result_len:
                result_len = end - begin
                result_start = begin
            begin += 1

    if result_len == float('inf'): return ""
    return s[result_start:result_len+result_start]

"""
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
"""
def findAnagrams(s, t):
    if len(t) > len(s):
        return ""
    # for key and value in m: if value == 0, means exact match
    m = {}
    for c in t:
        m[c] = m.get(c, 0) + 1

    count = len(m)
    begin = end = 0
    result = []

    while end < len(s):
        c = s[end]
        if c in m:
            m[c] -= 1
            if m[c] == 0:
                count -= 1
        end += 1

        while count == 0: # count = 0 means window is valid, we move start until window is invalid
            c = s[begin]
            if c in m:
                m[c] += 1
                if m[c] > 0:
                    count += 1
            # cuz is valid -> invalid, we need to record then update begin
            if end - begin == len(t):
                result.append(begin)
            begin += 1
    return result

"""
30. Substring with Concatenation of All Words
You are given a string, s, and a list of words, words, that are all of the same length.
 Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and 
 without any intervening characters.
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]

can simplify to find all anagrams in a string -> words => char
O(kn) k->length of each word
"""
import copy
def findSubstring(s, words):
    if not words or (words and len(words[0]) * len(words) > len(s)):
        return []
    c_len = len(words[0])
    # for key and value in m: if value == 0, means exact match
    word_m = {}
    for c in words:
        word_m[c] = word_m.get(c, 0) + 1

    result = set()
    for k in range(c_len):
        end = k
        begin = k
        count = len(word_m)
        m = copy.deepcopy(word_m)
        while end <= len(s):
            c = s[end - c_len:end]
            if c in m:
                m[c] -= 1
                if m[c] == 0:
                    count -= 1
            end += c_len

            while count == 0:  # count = 0 means window is valid, we move start until window is invalid
                c = s[begin:begin + c_len]
                if c in m:
                    m[c] += 1
                    if m[c] > 0:
                        count += 1

                if end - begin - c_len == len(words[0]) * len(words):
                    result.add(begin)
                begin += c_len
    return list(result)

"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
Input: "pwwkew"
Output: 3
"""
def lengthOfLongestSubstring(s):
    # for key and value in map, if value > 1 means repeat
    m = {}
    begin = end = 0
    count = len(m)
    result = 0

    while end < len(s):
        c = s[end]
        m[c] = m.get(c, 0) + 1
        if m[c] > 1:
            count += 1 # count means repeat char current in map, we need to make count = 1 -> valid
        end += 1
        while count > 0: # count > 0 means invalid, we want to make it tobe 0 -> valid
            c = s[begin]
            m[c] -= 1
            if m[c] >= 1:
                count -= 1
            begin += 1
        result = max(result, end - begin) # invalid -> valid, we need to record after update begin
    return result

"""
340. Longest Substring with At Most k Distinct Characters
Given a string s , find the length of the longest substring t  that contains at most k distinct characters.
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
"""
def lengthOfLongestSubstringKDistinct(s, k):
    result = 0
    m = {}
    count = len(m)
    begin = end = 0
    while end < len(s):
        # get a new char
        c = s[end]
        m[c] = m.get(c, 0) + 1
        if m[c] == 1:
            count += 1
        end += 1

        while count > k:
            c = s[begin]
            m[c] -= 1
            if m[c] == 0:
                count -= 1
            begin += 1
        result = max(result, end - begin)
    return result

"""
239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. Return the max sliding window.
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 

using deque
"""

def maxSlidingWindow(nums, k):
    if not nums:
        return []
    deque = []
    maxIdx = 0
    result = []
    for i in range(len(nums)):
        if deque and deque[0] < i - k + 1:
            deque.pop(0)
        while deque and nums[i] > nums[deque[-1]]:
            deque.pop()
        deque.append(i)
        result.append(nums[deque[0]])
    return result[k - 1:]