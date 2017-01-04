"""

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

"""

"""
1. Note it's the "permutation" of the string
2. The key character of a palindrome is that, there exists at most one character whose frequence is odd.
3. So we can use hash table to record all the frequncies and check the number of odd.

"""

import collections
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = collections.defaultdict(int)
        for c in s:
            lookup[c] += 1
        odds = sum([v % 2 == 1 for v in lookup.values()])
        return odds <= 1


    def canPermutePalindrome2(self, s):
        # soln 2: more elegant soln
        return sum(v % 2 for v in collections.Counter(s).values()) < 2