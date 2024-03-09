"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

https://leetcode.com/problems/number-of-islands/description/
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            We want to run a dfs or bfs algorithm on places in the grid with a 1. 

            however we only want to run this algorithm if the coordinate was not visited 
            before. that way we prevent incrementing the number of islands on adjacent nodes 
        """

        if not grid: 
            return 0
        rows, cols = len(grid), len(grid[0])
        visitedCoords = set()
        islands = 0

        def dfs(r,c):

            # Check that we are inbounds 
            if (
                c not in range(cols)
                or r not in range(rows)
                or grid[r][c] == "0"
                or (r,c) in visitedCoords
            ): return 

            visitedCoords.add((r,c))
            neighbors = [[0,-1], [0,1], [-1,0],[1,0]]

            for nr, nc in neighbors:
                dfs(r + nr, c +nc)

        for r in range(rows):   
            for c in range(cols):

                if grid[r][c] == "1" and (r,c) not in visitedCoords:
                    # First time we are seeing this piece of land
                    # Run bsf or dfs to mark all adjecent lands as visited 
                    dfs(r,c)
                    islands +=1 


        return islands


        