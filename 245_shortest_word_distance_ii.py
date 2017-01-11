#-*- coding: utf-8 -*-

"""

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.

"""

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_idx, word2_idx = float("inf"), float("inf")
        dist = len(words) - 1
        if word1 == word2:
            for i, w in enumerate(words):
                if w == word1:
                    dist = min(dist, abs(i - word1_idx))
                    word1_idx = i
            return dist
        else:
            for i, w in enumerate(words):
                if w == word1:
                    word1_idx = i
                elif w == word2:
                    word2_idx = i
                if word1_idx != float("inf") and word2_idx != float("inf"):
                    dist = min(dist, abs(word1_idx - word2_idx))
        return dist