# -*- coding: utf-8 -*-

"""

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

"""

# Time: O(n); Space: O(1)

import bisect

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = mid = float("inf")
        for n in nums:
            if n <= left:
                left = n
            elif n <= mid:
                mid = n
            else:
                return True
        return False

    """
    Generalize to k-uplet: use bisection algorithm
    """
    def increasingKUplet(self, nums, k):
        inc = [float('inf')] * (k - 1)
        for num in nums:
            i = bisect.bisect_left(inc, num)
            if i == k - 1:
                return True
            inc[i] = num
        return k == 0 # consider case of k = 0


if __name__ == "__main__":
    nums = [9, 8, 1, 10, 3, 0, 1, -10, 2, 8]

    print Solution().increasingTriplet(nums)
    print Solution().increasingKUplet(nums, 3)
    print Solution().increasingKUplet(nums, 4)
    print Solution().increasingKUplet(nums, 5)
