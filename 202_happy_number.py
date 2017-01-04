"""

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""

"""
Q:
    (1) constraints on algorithm?

Observation:
    (1) The only reason this process ends is that the last sum is 10, 100, 1000, etc.
    (2) Un-happy number will produce a cycle

Algorithm: Time: O(k); space: O(k); k is the steps to terminate loop
    (1) keep checking sum of squares of digits of n
    (2) if equal to 1 or has seen before, stop.

See also:

    wikipedia: https://en.wikipedia.org/wiki/Happy_number
    
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))

        return n == 1