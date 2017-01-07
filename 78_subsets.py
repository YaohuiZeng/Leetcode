"""

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        nums.sort()
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets

    def subsets2(self, nums):
        # soln 2: bit operations. Time: O(n * 2^n)
        n = len(nums)
        n_sub = 2 ** n
        subsets = [[] for _ in range(n_sub)]
        for i in range(n):
            for j in range(n_sub):
                if (j >> i) & 1:
                    subsets[j].append(nums[i])
        return subsets

if __name__ == "__main__":
    nums = [1, 2, 3]
    print Solution().subsets(nums)
    print Solution().subsets2(nums)


