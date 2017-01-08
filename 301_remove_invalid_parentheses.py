"""

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def is_valid2(s):
            s = filter(lambda x: x in "()", s)
            while "()" in s:
                s = s.replace("()", "")
            return not s

        level = {s}
        while True:
            valid = filter(is_valid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

if __name__ == "__main__":
    s = "(a)())()"
    print Solution().removeInvalidParentheses(s)
