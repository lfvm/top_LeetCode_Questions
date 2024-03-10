"""
130. Surrounded Regions


Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

https://leetcode.com/problems/surrounded-regions/description/

Input: board = [
                  ["X","X","X","X"],
                  ["X","O","O","X"],
                  ["X","X","O","X"],
                  ["X","O","X","X"]
                ]
Output:        [
                  ["X","X","X","X"],
                  ["X","X","X","X"],
                  ["X","X","X","X"],
                  ["X","O","X","X"]
                ]
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r,c):            
            if (
                r < 0 
                or r == rows
                or c < 0 
                or c == cols 
                or board[r][c] != 'O'
            ): return 

            board[r][c] = 'T'
            directions = [[0,1],[0,-1],[-1,0],[1,0]]
            for dr, dc in directions:
                dfs(r+dr,c+dc)



        """
            We know that the O on the border can not be changed
            so for now we are going to mark the border with Ts and 
            also adjacent coordinates
        """
        for r in range(rows):
            for c in range(cols):       
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r,c)


        # Now only remaininng O in the grid are the ones that 
        # we actually need to change
        for r in range(rows):
            for c in range(cols):       
                if board[r][c] == "O":
                    board[r][c] = 'X'

        # Reverse the chnages 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"