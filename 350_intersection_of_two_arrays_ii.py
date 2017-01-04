"""

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot
load all elements into the memory at once?

"""

import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # soln 1: hash table, defaultdict, 46 ms
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        lookup = collections.defaultdict(int)
        for num in nums1:
            lookup[num] += 1

        res = []
        for num in nums2:
            if lookup[num] > 0:
                res.append(num)
                lookup[num] -= 1
        return res
        """
        # soln 1: hash table, 78 ms
        n1, n2 = len(nums1), len(nums2)
        hash1, hash2 = {}, {}
        res = []
        for num in nums1:
            if num in hash1:
                hash1[num] += 1
            else:
                hash1[num] = 1
        for num in nums2:
            if num in hash2:
                hash2[num] += 1
            else:
                hash2[num] = 1

        if n1 <= n2:
            for num in hash1.keys():
                if num in hash2.keys():
                    res.extend([num] * min(hash1[num], hash2[num]))
        else:
            for num in hash2.keys():
                if num in hash1.keys():
                    res.extend([num] * min(hash1[num], hash2[num]))
        return res
        """

    def intersect2(self, nums1, nums2):
        # soln 2; sorted arrays, 65 ms
        n1, n2 = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        res = []
        p1, p2 = 0, 0
        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res