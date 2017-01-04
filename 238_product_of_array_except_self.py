"""

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose
 of space complexity analysis.)


"""

"""
Q:
    (1) could have zero:
        (i) if only 1 zero at position i, output[i] != 0; all others = 0
        (ii) if more than 1 zero, all output = 0
    (2) is x^(-1) cheating?


Soln 2:
    (1) input:  [a1, a2, a3, a4]
        output: [a2*a3*a4, a1*a3*a4, a1*a2*a4, a1*a2*a3]
             =  [1,        a1,       a1*a2,    a1*a2*a3]
             *  [a2*a3*a4, a3*a4,    a4,       1       ]

"""
import operator

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # soln 1: use x ** (-1). Time: O(n); space: O(n)
        n = len(nums)
        res = [0] * n
        zero_ind = [i for i in range(n) if nums[i] == 0]
        nonzeros = [x for x in nums if x != 0]

        if len(zero_ind) == 0:
            tot_prod = reduce(operator.mul, nums)
            for i in range(n):
                res[i] = int(tot_prod * nums[i] ** (-1))

        elif len(zero_ind) == 1:
            tot_prod = reduce(operator.mul, nonzeros)
            res[zero_ind[0]] = tot_prod

        return res


    def productExceptSelf2(self, nums):

        # soln 2: Time: O(n); space: O(n)
        n = len(nums)
        cum_left, cum_right, ret = [1] * n, [1] * n, [1] * n
        for i in range(1, n):
            cum_left[i] = cum_left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            cum_right[i] = cum_right[i + 1] * nums[i + 1]

        for i in range(n):
            ret[i] = cum_left[i] * cum_right[i]

        return ret

    def productExceptSelf3(self, nums):

        # soln 3: Time: O(n); space: O(1)
        n = len(nums)
        ret = [1] * n
        for i in range(1, n):
            ret[i] = ret[i - 1] * nums[i - 1]

        tmp = 1
        for i in range(n - 2, -1, -1):
            tmp *= nums[i + 1]
            ret[i] = ret[i] * tmp

        return ret

if __name__ == "__main__":
    nums = [1, 3, 4, 5, 2, 9]

    print Solution().productExceptSelf(nums)
    print Solution().productExceptSelf2(nums)
    print Solution().productExceptSelf3(nums)
