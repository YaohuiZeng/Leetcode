"""

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

"""
from collections import defaultdict

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m, l = len(A), len(B), len(B[0])
        res = [[0] * l for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if A[i][j]:
                    for k in range(l):
                        if B[j][k]:
                            res[i][k] += A[i][j] * B[j][k]
        return res

    # one hash table to store non-zero elements of B
    def multiply2(self, A, B):
        n, m, l = len(A), len(B), len(B[0])
        res = [[0] * l for _ in range(n)]

        tab_B = defaultdict(lambda: defaultdict(int))
        for j, row in enumerate(B):
            for k, elem in enumerate(row):
                if elem:
                    tab_B[j][k] = elem

        for i in range(n):
            for j in range(m):
                if A[i][j]:
                    if j in tab_B:
                        for k in tab_B[j]:
                            res[i][k] += A[i][j] * tab_B[j][k]
        return res

    # two hash tables to store non-zero elements of A and B
    def multiply3(self, A, B):
        n, m, l = len(A), len(B), len(B[0])
        tab_A, tab_B = defaultdict(lambda: defaultdict(int)), defaultdict(lambda: defaultdict(int))
        res = [[0] * l for _ in range(n)]

        for i, row in enumerate(A):
            for j, elem in enumerate(row):
                if elem:
                    tab_A[i][j] = elem

        for j, row in enumerate(B):
            for k, elem in enumerate(row):
                if elem:
                    tab_B[j][k] = elem

        for i in tab_A:
            for j in tab_A[i]:
                if j in tab_B:
                    for k in tab_B[j]:
                        res[i][k] += tab_A[i][j] * tab_B[j][k]
        return res