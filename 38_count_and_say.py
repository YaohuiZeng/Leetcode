"""

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        if n == 1:
            return "1"

        res = ""
        res_prev = self.countAndSay(n - 1)
        cur, count = res_prev[0], 1
        for i in range(1, len(res_prev)):
            if res_prev[i] != cur:
                res += str(count) + cur
                cur = res_prev[i]
                count = 1
            else:
                count += 1
        res += str(count) + cur
        return res


if __name__ == "__main__":

    print Solution().countAndSay(4)