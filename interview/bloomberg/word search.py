"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

# backtracking

class Solution(object):
    def search_word_util(self, board, row, col, word):
        if len(word) == 0:
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0]:
            return False

        board[row][col] = "#"

        if self.search_word_util(board, row - 1, col, word[1:]):
            return True
        if self.search_word_util(board, row + 1, col, word[1:]):
            return True
        if self.search_word_util(board, row, col - 1, word[1:]):
            return True
        if self.search_word_util(board, row, col + 1, word[1:]):
            return True

        board[row][col] = word[0]
        return False



    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            for j in range(len(word[0])):
                if self.search_word_util(board, i, j, word):
                    return True
        return False


class Solution2(object):
    def exist(self, board, word):
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


