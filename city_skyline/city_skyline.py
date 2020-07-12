# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

# 807. Max Increase to Keep City Skyline

# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there.
# We are allowed to increase the height of any number of buildings, by any amount
# (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 
# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right,
# must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles
# formed by all the buildings when viewed from a distance. See the following example.
# What is the maximum total sum that the height of the buildings can be increased?

class Solution:
    result = 0

    def maxIncreaseKeepingSkyline(self, grid: [[int]]) -> int:
        inv_grid = [[] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid)):
                inv_grid[j] += [grid[i][j]]

        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in inv_grid]

        for i in range(len(grid)):
            for j in range(len(inv_grid)):
                if (grid[i][j] == row_maxes[i] or grid[i][j] == col_maxes[j]):
                    continue
                self.result += min(row_maxes[i], col_maxes[j]) - grid[i][j]

        return self.result