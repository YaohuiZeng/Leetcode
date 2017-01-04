"""

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up
to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

"""

"""
Algorithm: dynamic programming

"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def comb(nums, target, lookup):
            res = 0
            if target == 0:
                return 1
            if target < 0:
                return 0
            for num in nums:
                if num > target:
                    break
                if target - num in lookup:
                    res += lookup[target - num]
                else:
                    val = comb(nums, target - num, lookup)
                    lookup[target - num] = val
                    res += val
            return res

        nums.sort()
        lookup = {}
        return comb(nums, target, lookup)

if __name__ == "__main__":
    nums = [4, 2, 1]
    target = 32
    print Solution().combinationSum4(nums, target)