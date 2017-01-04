"""

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.


"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_map, res_map = {}, {}
        for num in nums1:
            if not num in nums1_map:
                nums1_map[num] = 1
        for num in nums2:
            if num in nums1_map and (not num in res_map):
                res_map[num] = 1
        return res_map.keys()

    def intersection2(self, nums1, nums2):

        # soln 2: sorting
        nums1.sort()
        nums2.sort()
        res = []
        i1, i2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while i1 < n1 and i2 < n2:
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                if res:
                    if res[-1] != nums1[i1]:
                        res.append(nums1[i1])
                else:
                    res.append(nums1[i1])
                i1 += 1
                i2 += 1
        return res
