"""

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

"""

"""
Q:
    (1) could have 0, and negative
    (2) input contains at least one number
    (3) all integers?

Algorithm: Time: O(n); Space: O(1). https://www.quora.com/How-do-I-solve-maximum-product-subarray-problems

    You have three choices to make at any position in array.
    1. You can get maximum product by multiplying the current element with
        maximum product calculated so far.  (might work when current
        element is positive).
    2. You can get maximum product by multiplying the current element with
        minimum product calculated so far. (might work when current
        element is negative).
    3.  Current element might be a starting position for maximum product sub
         array

"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_max, prev_min, cur_max, res = nums[0], nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
            cur_min = min(prev_max * nums[i], prev_min * nums[i], nums[i])
            res = max(cur_max, res)
            prev_max, prev_min = cur_max, cur_min

        return res
