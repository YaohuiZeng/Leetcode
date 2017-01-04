"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.

"""

"""
special case: [1, 0, 1, 1] k = 1, expected: True


"""



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for i in range(len(nums)):
            if nums[i] in table and i - table[nums[i]] <= k:
                    return True
            else:
                table[nums[i]] = i #  update to newly occurred index for special case [1, 0, 1, 1] k = 1
        return False