"""

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

"""

"""
1. use python in-place sort()
2. one pass: compare current and next, if not the right order, swap.
    This works because: suppose we already have nums[0] <= nums[1] in the right order. Then when comparing nums[1]
    and nums[2], if nums[1] < nums[2], meaning the required ">=", we swap nums[1] and nums[2], the first "<=" still
    holding because nums[2] > nums[1] >= nums[0].
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        for i in range(1, n-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

    def wiggleSort2(self, nums):
        for i in range(0, len(nums)-1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]