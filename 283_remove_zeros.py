"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_ind = 0
        while zero_ind < n and nums[zero_ind] != 0:
            zero_ind += 1
        nonzero_ind = zero_ind + 1
        while nonzero_ind < n and nums[nonzero_ind] == 0:
            nonzero_ind += 1
        while nonzero_ind < n:
            nums[zero_ind], nums[nonzero_ind] = nums[nonzero_ind], nums[zero_ind]
            zero_ind += 1
            while zero_ind < n and nums[zero_ind] != 0:
                zero_ind += 1
            nonzero_ind += 1
            while nonzero_ind < n and nums[nonzero_ind] == 0:
                nonzero_ind += 1

    def moveZeros2(self, nums):
        n = len(nums)
        zero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1