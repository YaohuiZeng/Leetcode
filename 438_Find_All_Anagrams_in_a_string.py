"""

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


"""
from collections import Counter, defaultdict

class Solution(object):

    # brute-force: time: O()
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res, len_p = [], len(p)
        if len(s) < len_p:
            return []

        lookup = Counter(p)
        for i in xrange(len(s)):
            if Counter(s[i:(i + len_p)]) == lookup:
                res.append(i)
        return res

    # sliding window: O(n)
    def findAnagrams2(self, s, p):
        res = []
        len_p, len_s = len(p), len(s)
        if len_s < len_p: return res

        lookup = defaultdict(int)
        for c in p:
            lookup[c] += 1

        left, right, count = 0, 0, len_p
        while right < len_s:
            if lookup[s[right]] >= 1: count -= 1
            lookup[s[right]] -= 1
            right += 1

            if count == 0: res.append(left)

            if right - left == len_p:
                if lookup[s[left]] >= 0:
                    count += 1
                lookup[s[left]] += 1
                left += 1

        return res


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    # s = "abab"
    # p = "ab"
    print Solution().findAnagrams1(s, p)
    print Solution().findAnagrams2(s, p)






