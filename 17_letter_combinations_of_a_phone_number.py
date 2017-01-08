"""

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

## Assume no 0 nor 1 in input digits.
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        lookup = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = ['']
        for d in digits:
            tmp = []
            for r in res:
                tmp.extend(r + s for s in lookup[d])
            res = tmp
        return res

    def letterCombinations2(self, digits):
        if len(digits) == 0:
            return []
        lookup = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                  "9": "wxyz"}
        res = ['']
        for d in digits:
            res = [r + s for r in res for s in lookup[d]]
        return res

if __name__ == "__main__":
    digits = '23'
    print Solution().letterCombinations(digits)
    print Solution().letterCombinations2(digits)