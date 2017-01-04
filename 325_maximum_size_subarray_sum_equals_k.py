"""

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one,
return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

"""

"""

Q:
    (1) note "subarray": consecutive elements
    (2) note "maximum" length

Observation:
    (1) input: nums = [1, -1, 5, -2, 3], k = 3.
    (2) Given "consecutive elements" constraint, suppose there exists 0<=i<=j<n such that sum(nums[i:j]) = k, then it
        must be that sum(nums[:j]) - sum(nums[:i]) = k.
    (3) thus, we can check whether the difference of cumulative sum at j and that at i is equal to k. If true, [i+1, j]
        must be the subarray

Algorithm: "prefix sum" + hash table. Time: O(n); Space: O(n)
    (1) initialize:
            max_len: the result to return
            prefix_sum: the hash table to store the prefix sum at each index i, key = prefix_sum at index i (including i);
            value = index i
    (2) At each index i, compute prefix sum, named sum. If not in hash table, put it in. Then check whether sum - k is
        seen in table. if true, update max_len = max(max_len, i - prefix_sum[sum-k]).
            Note: the difference of the two indices is exactly the length of subarray. HOWEVER, if sum == k, that is,
            the subarry starts at 0, that difference would exclude 1 element. This can be fixed by either
            update max_len = max_len + 1 or (preferred) initialize prefix_sum = {0:-1}, i.e., the prefix sum before
            index 0 is 0 with index -1.
    (3) If sum is in hash table, that means there is a subarray with sum of 0 in between. We don't want to update the
        value (i.e., index) in the hash table since we need the maximum length of subarray.

"""

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur_sum, max_len = 0, 0
        prefix_sum = {0: -1}

        for i in xrange(len(nums)):
            cur_sum += nums[i]
            if cur_sum not in prefix_sum:
                prefix_sum[cur_sum] = i
            if cur_sum - k in prefix_sum:
                max_len = max(max_len, i - prefix_sum[cur_sum - k])

        return max_len
    