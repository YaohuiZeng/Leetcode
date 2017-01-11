# -*- coding: utf-8 -*-

"""

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

"""

"""
Q:
    (1) there may be duplicated word1 and word2
    (2) word1 != word2, and both exist
"""

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(words)
        word1_idx, word2_idx = None, None
        distance = n-1
        for i, w in enumerate(words):
            if w == word1:
                word1_idx = i
            elif w == word2:
                word2_idx = i
            if word1_idx is not None and word2_idx is not None:
                distance = min(distance, abs(word1_idx-word2_idx))
        return distance