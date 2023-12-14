'''
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

 

Example 1:


Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
Example 2:


Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.
Example 3:


Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
'''
from ast import List

class Solution:

    def tictactoe(self, moves: List[List[int]]) -> str:

        # check winner
        def check_winner(board, player_symbol):
            # check rows and cols
            for i in range(3):
                if all(board[i][j] == player_symbol for j in range(3)) or all(board[j][i] == player_symbol for j in range(3)):
                    return True
            # check diagonals
            if all(board[i][i] == player_symbol for i in range(3)) or all(board[i][2-i] == player_symbol for i in range(3)):
                return True
            return False

        x_moves = list()
        o_moves = list()
        res = ""
        
        # build board
        board = [[' ' for _ in range(3)] for _ in range(3)]
        for move_ind in range(len(moves)):
            if move_ind % 2 == 0:
                x_moves.append(moves[move_ind])
                board[moves[move_ind][0]][moves[move_ind][1]] = 'X'
            else: 
                o_moves.append(moves[move_ind])
                board[moves[move_ind][0]][moves[move_ind][1]] = 'O'

        if len(x_moves) == 5 or len(x_moves) > len(o_moves):
            if check_winner(board, 'X'):
                return "A"
        else:
            if check_winner(board, 'O'):
                return "B"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"


    
