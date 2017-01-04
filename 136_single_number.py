"""

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

"""
1. Bitwise XOR sets the bits in the result to 1 if either, but not both, of the corresponding bits in the two operands is 1.
2. Bitwise XOR is commutative: A XOR B XOR C = C XOR B XOR A.
3. A XOR A = 0

So for the problem, suppose we have [1, 1, 2, 3, 4, 3, 2], applying XOR iteratively yields:
1 ^ 1 ^ 2 ^ 3 ^ 4 ^ 3 ^ 2 = 1 ^ 1 ^ 2 ^ 2 ^ 3 ^ 3 ^ 4 = 0 ^ 4 = 4

Ex.: swap two variables without temp by using XOR
x, y = 2, 8
x ^= y (= b10 ^ b1000 = b1010 = 10)
y ^= x (= b1000 ^ b1010 = b10 = 2, i.e., y = y ^ x ^ y = y ^ y ^ x = x)
x ^= y (= b1010 ^ b10 = b1000 = 8, i.e., x = (x ^ y) ^ (y ^ x ^ y) = y

or: x, y = x ^ y ^ x, y ^ x ^ y

"""


import collections
import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # soln 1: use extra space. Time: O(n); Space: O(n)
        lookup = collections.Counter(nums)
        return lookup.keys()[lookup.values().index(1)]


    def singleNumber2(self, nums):

        # soln 2: bit XOR. Time: O(n); Space: O(1)
        res = 0
        for n in nums:
            res ^= n
        return res

    def singleNumber3(self, nums):

        # soln 3: use reduce()
        # return reduce(lambda x, y: x ^ y, nums)
        return reduce(operator.xor, nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 4, 1, 3]
    s = Solution()
    print s.singleNumber(nums)
    print s.singleNumber2(nums)
    print s.singleNumber3(nums)