"""

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume
that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

"""

import random
import collections

# init time: O(1); Space: O(n); Pick time: O(n)

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indices = [i for i, v in enumerate(self.nums) if v == target]
        return random.choice(indices)


    """
    reservoir sampling
    """
    def pick2(self, target):
        res, count = -1, 0
        for i, v in enumerate(self.nums):
            if v == target:
                if random.randint(0, count) == 0:
                    res = i
                count += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


## this exceeds memory limit, though, when data is large
# Init time: O(n); Space: O(n); Pick time: O(1)
class Solution2(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.lookup = collections.defaultdict(list)
        for i, v in enumerate(nums):
            self.lookup[v].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.lookup[target])

if __name__ == "__main__":
    nums = [1, 2, 3, 3, 4, 4, 4, 4, 5]
    print Solution(nums).pick(1), Solution(nums).pick2(1), Solution2(nums).pick(1)
    print Solution(nums).pick(4), Solution(nums).pick2(4), Solution2(nums).pick(4)
    print Solution(nums).pick(5), Solution(nums).pick2(5), Solution2(nums).pick(5)

