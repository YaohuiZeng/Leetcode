"""

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes"
(water inside that isn't connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

"""





class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lookup = {}
        rows = len(grid)
        cols = len(grid[0])

        ones, overlaps = 0, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ones += 1
                    lookup[(i, j)] = 1
                    if (i - 1, j) in lookup:
                        overlaps += 1
                    if (i + 1, j) in lookup:
                        overlaps += 1
                    if (i, j - 1) in lookup:
                        overlaps += 1
                    if (i, j + 1) in lookup:
                        overlaps += 1
        return 4 * ones - 2 * overlaps


    # or don't need temp variables, ones and overlaps.
    def islandPerimeter2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lookup = {}
        rows = len(grid)
        cols = len(grid[0])

        p = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    p += 4
                    lookup[(i, j)] = 1
                    if (i - 1, j) in lookup:
                        p -= 2
                    if (i + 1, j) in lookup:
                        p -= 2
                    if (i, j - 1) in lookup:
                        p -= 2
                    if (i, j + 1) in lookup:
                        p -= 2
        return p


    # since search from upper-left to bottom-right, no need to check (i+1, j) and (i, j+1) cells!!
    def islandPerimeter3(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lookup = {}
        rows = len(grid)
        cols = len(grid[0])

        p = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    p += 4
                    lookup[(i, j)] = 1
                    if (i - 1, j) in lookup:
                        p -= 2
                    if (i, j - 1) in lookup:
                        p -= 2
        return p