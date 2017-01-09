"""

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's
and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

"""


class Solution(object):

    # insertion sort
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            j = i
            while j and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1


    def sortColors2(self, nums):
        # bubble sort
        n = len(nums)
        for i in range(0, n-1):
            for j in range(1, n-i):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]

    # one pass: three pointers
    def sortColors3(self, nums):
        n = len(nums)
        zero, second = 0, n-1
        for i in xrange(n):
            while nums[i] == 2 and i < second:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
