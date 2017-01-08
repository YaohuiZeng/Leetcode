"""

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""

class Solution(object):
    def get_elem(self, row, pos):
        if row in [0, 1] or pos in [0, row]:
            return 1
        else:
            return self.get_elem(row - 1, pos - 1) * row / pos

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(rowIndex + 1):
            res.append(self.get_elem(rowIndex, i))
        return res

    def getRow2(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                res[j] += res[j-1]
        return res

if __name__ == "__main__":
    print Solution().getRow(5)
    print Solution().getRow2(5)
