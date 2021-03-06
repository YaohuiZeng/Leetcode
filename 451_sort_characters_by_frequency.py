"""

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""

import collections

class Solution(object):

    # soln 1: use python Counter class, and most_common() function
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s).most_common()
        return "".join(key * val for key, val in count)

    # soln 2: use sorted function. Time: O(nlog(n)); space: O(n)
    def frequencySort2(self, s):
        # soln 2: sorted
        lookup = collections.defaultdict(int)
        for c in s:
            lookup[c] += 1
        count = sorted(lookup.items(), key=lambda x: x[1], reverse=True)
        return "".join(key * val for key, val in count)

    # soln 3: build another list of substrings in which the index is the frequency of the characters (in the substring).
    #       Time: O(n); Space: O(n)
    def frequencySort3(self, s):
        lookup = collections.defaultdict(int)
        for c in s:
            lookup[c] += 1
        count = [""] * (len(s)+1)
        for k in lookup:
            count[lookup[k]] += k
        res = ""
        for i in range(len(count)-1, -1, -1):
            if count[i] == "": continue
            for c in count[i]:
                res += c * i
        return res

if __name__ == "__main__":

    s = 'ttreee'
    print Solution().frequencySort(s)
    print Solution().frequencySort2(s)