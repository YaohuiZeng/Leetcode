"""

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

"""

"""
Q:
    (1) at least one number
    (2) return sum?
    (3) it's possible to have multiple solutions due to 0 or "sum to 0". return the subarray with smallest length?
    (4) can all be negative?

Algorithm: brute-force. Time: O(n^2), space: O(1)
    (1) given i, find max_sum of all subarrays starting with i
    (2) loop over i

observation:
    (1) the optimal subarray must be starting and ending with positive (non-negative); otherwise, we can chop off that number to produce a better one. (Wrong. Because could all be negative numbers)
    (2) Suppose the subarray is A[i:j), where 0<=i<=j<=n, then it must be that A[:i) <= 0 and A[j:) <= 0 (right)

Algorithm 2: Kandane's algorithm. Time: O(n); Space: O(1)

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # soln 1:
        n = len(nums)
        max_sum = -float("inf")
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                max_sum = max(cur, max_sum)
        return max_sum

    def maxSubArray2(self, nums):
        i, n = 0, len(nums)
        sum_i, max_sum_i = 0, -float("inf")
        while i < n:
            sum_i += nums[i]
            max_sum_i = max(max_sum_i, sum_i)
            if sum_i <= 0:
                sum_i = 0
            i += 1

        return max_sum_i

if __name__== "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [-1, -2, -3]
    # nums = [1, 2, 3]
    print Solution().maxSubArray(nums)
    print Solution().maxSubArray2(nums)