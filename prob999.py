# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

# Return the number of pawns the rook can capture in one move.


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        x, y, r_found = 0,0, False
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    x, y = i, j
                    r_found = True 
                    break
            if r_found: 
                break 
        up = self.helper(board, i, j, 1)
        down = self.helper(board, i, j, 2)
        left = self.helper(board, i, j, 3)
        right = self.helper(board, i, j, 4)
        return up + down + left + right 
    
    
    def helper(self, board: List[List[str]], i: int, j: int, direction: int) -> int:
        if i < 0 or j < 0 or i >= 8 or j >= 8: return 0 
        if board[i][j] == 'B': return 0 
        if board[i][j] == 'p': return 1 
        if direction == 1: return self.helper(board, i-1, j, 1)
        if direction == 2: return self.helper(board, i+1, j, 2)
        if direction == 3: return self.helper(board, i, j-1, 3)
        if direction == 4: return self.helper(board, i, j+1, 4)
