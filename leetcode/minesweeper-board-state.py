'''
Problem Link: https://leetcode.com/problems/minesweeper/description/

'''
from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        # return board with X when clicked a mine
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        # set directions for neighbouring cells
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1, -1), (-1, 1)]

        # count mines
        def countMines(row, col):
            count = 0
            for r,c in directions:
                # check bounds and cell value
                if 0 <= row+r < len(board) and 0 <= col+c < len(board[0]) and board[row+r][col+c] == 'M':
                    count += 1
            return count

        # update board using dfs
        def dfs(row, col):
            # if row, col out of bounds, exit
            if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != 'E':
                return
            
            mines = countMines(row, col)
            # set mines 'M' or blank 'B' and continue neighbour search
            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for r,c in directions:
                    dfs(row+r, col+c)
        
        # initiate dfs on row,col passed
        dfs(click[0], click[1])
        
        return board

s = Solution()
print(s.updateBoard([["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], [1,2]))
