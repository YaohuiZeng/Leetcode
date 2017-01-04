# -*- coding: utf-8 -*-

"""

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.


"""

"""
Q:
    (1) could there be duplicates? [1, 2, 3, 3, 4, 5, 5], 1st: 5, 2nd: 5, 3rd: 4, 4th: 3...
    (2) can I use built-in sort()?

Algorithm 1: use built-in sort(). Time: O(nlog(n)); Space: O(1)
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]

