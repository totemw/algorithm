"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G),and white(W).
You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row
(including the leftmost place and rightmost place).
Then, if there is a group of 3 or more balls in the same color touching, remove these balls.
Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table.
If you cannot remove all the balls, output -1.

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
"""

# DFS + hash

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        hash = {
            'R': 0,
            'Y': 0,
            'B': 0,
            'G': 0,
            'W': 0
        }

        for ball in hand:
            hash[ball] += 1


        def DFS(board, hash):
            if not board:
                return 0
            result = float("inf")
            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1
                sameBall = 3 - (j - i)
                if sameBall < 0:
                    sameBall = 0

                if hash[board[i]] >= sameBall:
                    hash[board[i]] -= sameBall
                    if DFS(board[:i] + board[j:], hash) >= 0:
                        result = min(sameBall + DFS(board[:i] + board[j:], hash), result)
                    hash[board[i]] += sameBall

                i = j

            if result == float("inf"):
                return -1
            else:
                return result

        return DFS(board, hash)
