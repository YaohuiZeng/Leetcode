"""

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?


Hint:

A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.


"""

"""
1. If a number is less than 10, return number; otherwise
2. If a number can be divided by 9, return 9; otherwise
3. return mod

See wikipedia: https://en.wikipedia.org/wiki/Digital_root



"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        div, mod = num // 10, num % 10
        while div:
            num = div + mod
            div, mod = num // 10, num % 10
        return mod

    def addDigits2(self, num):

        while num // 10:
            num = (num // 10) + (num % 10)
        return num % 10

    # soln 3: see wikipedia
    def addDigits3(self, num):
        if num < 10:
            return num

        div, mod = num // 9, num % 9
        if mod:
            return mod
        else:
            return 9

if __name__ == "__main__":

    num = 38083545525

    print Solution().addDigits(num)
    print Solution().addDigits2(num)
    print Solution().addDigits3(num)
