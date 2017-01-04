"""

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""

import math

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        lower, upper = 1, int(math.sqrt(2 * n)) + 1
        while lower < upper:
            mid = (lower + upper) // 2

            if mid * mid + mid - 2 * n < 0:
                lower = mid + 1
            elif mid * mid + mid - 2 * n == 0:
                return mid
            elif mid * mid + 3 * mid + 2 - 2 * n > 0:
                upper = mid
            else:
                return mid - 1
        return lower - 1

    def arrangeCoins2(self, n):
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if 2 * n < mid * (mid+1):
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
