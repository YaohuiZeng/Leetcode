"""
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = second_max = third_max = -float("Inf")
        for i in range(len(nums)):
            if nums[i] > first_max:
                third_max = second_max
                second_max = first_max
                first_max = nums[i]
            elif nums[i] > second_max and nums[i] != first_max:
                third_max = second_max
                second_max = nums[i]
            elif nums[i] > third_max and nums[i] != second_max and nums[i] != first_max:
                third_max = nums[i]
        return third_max if not third_max == -float("Inf") else first_max