"""

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def DFS(grid, visited, i, j, m, n):
            if i < 0 or i > n - 1 or j < 0 or j > m - 1 or visited[i][j] or grid[i][j] != "1":
                return
            visited[i][j] = 1
            DFS(grid, visited, i + 1, j, m, n)
            DFS(grid, visited, i - 1, j, m, n)
            DFS(grid, visited, i, j + 1, m, n)
            DFS(grid, visited, i, j - 1, m, n)

        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    DFS(grid, visited, i, j, m, n)
                    count += 1
        return count