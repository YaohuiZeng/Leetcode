"""

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

"""

# Space O(n); time O(n)

# if O(1) space required, can first do heap-sort, then compare adjacent elements, O(nlog(n)) time

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for n in nums:
            if n in nums_dict:
                return True
            else:
                nums_dict[n] = 1
        return False
