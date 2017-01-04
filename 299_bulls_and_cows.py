"""

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to
guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits
in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match
the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints
to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and
B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

"""

import collections

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = [int(i) for i in secret], [int(j) for j in guess]
        diff = [vs - vg for vs, vg in zip(s, g)]
        bull_idx = [i for i in range(len(diff)) if diff[i] == 0]
        b = len(bull_idx)

        s_m = collections.defaultdict(int)
        for i in range(len(s)):
            if i not in bull_idx:
                s_m[s[i]] += 1

        c = 0
        for j in range(len(g)):
            if j not in bull_idx and s_m[g[j]] > 0:
                c += 1
                s_m[g[j]] -= 1
        res = str(b) + "A" + str(c) + "B"
        return res

    def getHint2(self, secret, guess):
        # better soln
        b, c = 0, 0
        st = collections.defaultdict(int)
        gt = collections.defaultdict(int)

        for s, g in zip(secret, guess):
            if s == g:
                b += 1
            else:
                if st[g]:
                    c += 1
                    st[g] -= 1
                else:
                    gt[g] += 1
                if gt[s]:
                    c += 1
                    gt[s] -= 1
                else:
                    st[s] += 1

        return "{}A{}B".format(b, c)
