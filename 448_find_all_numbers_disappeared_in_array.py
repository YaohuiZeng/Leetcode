# -*- coding: utf-8 -*-

"""

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""

"""
Algorithm:
    (1) For each number i in nums, mark the number that i points as negative.
    (2) Then get all the indices who points to a positive number. These indices are not visited.

"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            nums[ind] = - abs(nums[ind])
        res = [i+1 for i, num in enumerate(nums) if num > 0]
        return res
