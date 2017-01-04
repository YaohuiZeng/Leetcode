"""

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if flag:
                if digits[i] == 9:
                    res.append(0)
                    flag = 1
                else:
                    res.append(digits[i]+1)
                    flag = 0
            else:
                res.append(digits[i])
        if flag:
            res.append(1)
        res.reverse()
        return res