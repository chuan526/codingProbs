# On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

# Now we view the projection of these cubes onto the xy, yz, and zx planes.

# A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

# Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

# Return the total area of all three projections.


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = xz = yz = 0 
        for i in range(len(grid)):
            xz += max(grid[i])
            yz_col = 0 
            for j in range(len(grid[0])):
                if grid[i][j]: xy += 1 
                yz_col = max(grid[j][i], yz_col)
            yz += yz_col 
        return xz + xy + yz 
  
