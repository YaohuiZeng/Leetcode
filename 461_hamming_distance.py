# -*- coding: utf-8 -*-

"""

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        res = list(bin(x ^ y))
        for c in res:
            if c == "1":
                count += 1
        return count

    def hammingDistance2(self, x, y):
        return sum(map(lambda c: c == "1", bin(x ^ y)))


if __name__ == "__main__":
    x, y = 2, 5
    print Solution().hammingDistance(x, y)
    print Solution().hammingDistance2(x, y)