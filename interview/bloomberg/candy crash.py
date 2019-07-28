"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j]
 represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty.
 The given board represents the state of the game following the player's move.
 Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.

After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)

After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.

If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.

You need to perform the above rules until the board becomes stable, then return the current board.

"""

# a crush step (negative => flag), and a gravity step (loop each column from bottom to head and swqp non zero)

class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        state = True

        R = len(board)
        C = len(board[0])

        for r in range(R - 2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    state = False

        for r in range(R):
            for c in range(C - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    state = False

        if state:
            return board
        else:
            for r in range(R):
                for c in range(C):
                    if board[r][c] < 0:
                        board[r][c] = 0

            for c in range(C):
                start = end = -1
                for r in range(R - 1, -1, -1):
                    if board[r][c] == 0:
                        start = r
                        end = r
                        break

                if start == -1:
                    continue

                while end >= 0:
                    if board[end][c] == 0:
                        end -= 1
                    else:
                        board[start][c], board[end][c] = board[end][c], board[start][c]
                        start -= 1
                        end -= 1
            return self.candyCrush(board)