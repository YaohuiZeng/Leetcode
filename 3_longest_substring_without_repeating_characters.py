"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
subsequence and not a substring.

"""

"""
Q:
    (1) input: substring, not subsequence
    (2) input: what type of character
    (3) input: could be null?
    (3) output: what to return? length? index? substring?
    (4) complexity?

Algorithm: two pointers. Time: O(n); Space: O(max(n+m)), where m is the size of charset. ASCII: 128; extended ASCII: 256
    (1) left pointer points to the start of substring; right pointer walks down as furthest as possible
    (2) need a hash table to store substring: key = character; value = index
    (3) Each time check current character that right pointer points to. If in table:
            len_substr = right - left; longest = max(longest, len_substr)
            reset left pointer right to position of the first occurrence of the repeated character;
            reset table: exclude characters appeared before the first occurrence of the repeated character
    (4) if not move right pointer until end

See also:

    Leetcode: https://leetcode.com/articles/longest-substring-without-repeating-characters/
    sliding window: A sliding window is an abstract concept commonly used in array/string problems. A window is a range
    of elements in the array/string which usually defined by the start and end indices, i.e. [i, j)[i,j) (left-closed,
    right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we
    slide [i, j)[i,j) to the right by 11 element, then it becomes [i+1, j+1)[i+1,j+1) (left-closed, right-open).
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        longest, i, j = 0, 0, 0
        substr = {}
        while j < n:
            if s[j] in substr and substr[s[j]] >= i:
                longest = max(longest, j - i)
                i = substr[s[j]] + 1
            substr[s[j]] = j
            j += 1

        longest = max(longest, j - i)

        return longest



