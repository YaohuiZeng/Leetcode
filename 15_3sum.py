"""

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

"""
Q:
    (1) input length must be no less than 3?


Algorithm:
    (1) sort the array
    (2) for a given i, find all possible triplets using nums[i] as its first element and have sum 0.
            then for each i. have two pointers left, and right.
            if nums[i] > 0, break the for loop since we won't be able to find such triplet.

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n, res = len(nums), []
        for i in xrange(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates
                continue
            if i > 0 and nums[i] > 0:  # won't find such triplets
                break

            left, right = i + 1, n - 1
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    nums = [0, 0, -2, -1, 0, 1, 2, -1, -1, 4]

    print Solution().threeSum(nums)
