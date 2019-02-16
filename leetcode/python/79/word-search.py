"""79. Word Search
Medium

1376

63

Favorite

Share

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent
cell, where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
Accepted
241,544
Submissions
804,388

"""

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    visited = [False] * m
                    for k in range(0, m):
                        visited[k] = [False] * n
                    if self.visit(
                        board, m, n,
                        word, 0, visited, i, j):
                        return True
        return False

    def visit(self, board, m, n, word, i, visited, y, x):
        # print(i, visited, y, x)
        if not ((0 <= y < m) and (0 <= x < n)):
            return False
        if visited[y][x]:
            return False
        if word[i] != board[y][x]:
            visited[y][x]
            return False

        # print("Found", word[i], i, word)
        if i == len(word) - 1:
            return True

        visited[y][x] = True

        if (
                self.visit(
                    board, m, n, word, i+1, visited, y+1, x) or
                self.visit(
                    board, m, n, word, i+1, visited, y-1, x) or
                self.visit(
                    board, m, n, word, i+1, visited, y, x+1) or
                self.visit(
                    board, m, n, word, i+1, visited, y, x-1)):
            return True
        else:
            visited[y][x] = False
            return False


s = Solution()
if False:
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(s.exist(board, "ABCCED"))
    print(s.exist(board, "SEE"))
    print(s.exist(board, "ABCB"))

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'E', 'S'],
    ['A', 'D', 'E', 'E']
]
print(s.exist(board, "ABCESEEEFS"))
