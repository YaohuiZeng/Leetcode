"""

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        ai = [int(i) for i in a][::-1]
        bi = [int(i) for i in b][::-1]

        i, carryover = 0, 0
        while i < len(ai) or i < len(bi):
            val = carryover
            if i < len(ai):
                val += ai[i]
            if i < len(bi):
                val += bi[i]
            val, carryover = val % 2, val // 2
            res.append(val)
            i += 1

        if carryover:
            res.append(1)
        res.reverse()
        return "".join(str(c) for c in res)

    def addBinary2(self, a, b):
        # soln 2: use stack
        res = []
        a, b = map(int, a), map(int, b)
        carryover = 0
        while a or b:
            val = carryover
            if a:
                val += a.pop()
            if b:
                val += b.pop()
            val, carryover = val % 2, val // 2
            res.append(val)

        if carryover:
            res.append(1)

        return "".join(str(c) for c in reversed(res))


if __name__ == "__main__":
    a = "1011101"
    b = "1010"

    assert Solution().addBinary(a, b) == Solution().addBinary2(a, b)
    print Solution().addBinary(a, b)
    print Solution().addBinary2(a, b)

