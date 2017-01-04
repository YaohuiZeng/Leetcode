"""

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the
distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled
with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""


"""
Algorithm: Breadth-first search. Time: O(m*n)

"""

import collections

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        def dist_around(rooms, m, n, i, j, q):
            INF = 2147483647
            r = i + 1
            if r < m and rooms[r][j] == INF:
                rooms[r][j] = rooms[i][j] + 1
                q.append([r, j])

            r = i - 1
            if r >= 0 and rooms[r][j] == INF:
                rooms[r][j] = rooms[i][j] + 1
                q.append([r, j])

            c = j + 1
            if c < n and rooms[i][c] == INF:
                rooms[i][c] = rooms[i][j] + 1
                q.append([i, c])

            c = j - 1
            if c >= 0 and rooms[i][c] == INF:
                rooms[i][c] = rooms[i][j] + 1
                q.append([i, c])

        m = len(rooms)
        if m < 1:
            return
        n = len(rooms[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i, j])

        while q:
            room = q.popleft()
            dist_around(rooms, m, n, room[0], room[1], q)