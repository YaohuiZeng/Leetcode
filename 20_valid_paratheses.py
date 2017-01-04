"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Subscribe to see which companies asked this question

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2:
            return False
        buf = []
        lookup = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in lookup:
                if len(buf) == 0 or lookup[c] != buf.pop():
                    return False
            else:
                buf.append(c)
        return buf == []






