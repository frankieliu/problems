#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (21.87%)
# Total Accepted:    130.8K
# Total Submissions: 598.2K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
#
#
class Solution:
    def solve(self, b):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(b) < 3 or len(b[0]) < 3:
            return

        # do a dfs pass through all marked border O's
        # top
        for i in range(0, len(b[0])):
            if b[0][i] == 'O':
                # print("Found 0")
                self.visit(0, i, b)
            if b[len(b)-1][i] == 'O':
                # print("Found 1")
                self.visit(len(b)-1, i, b)

        for j in range(1, len(b)-1):
            if b[j][0] == 'O':
                # print("Found 2")
                self.visit(j, 0, b)
            if b[j][len(b[0])-1] == 'O':
                # print("Found 3")
                self.visit(j, len(b[0])-1, b)

        for j in range(0, len(b)):
            for i in range(0, len(b[0])):
                el = b[j][i]
                if el == 'O':
                    b[j][i] = 'X'
                elif el == 'b':
                    b[j][i] = 'O'

    def visit(self, j, i, b):
        if 0 <= i < len(b[0]) and 0 <= j < len(b):
            if b[j][i] == 'O':
                b[j][i] = 'b'
                self.visit(j, i-1, b)
                self.visit(j, i+1, b)
                self.visit(j-1, i, b)
                self.visit(j+1, i, b)

test = False
if test:
    a = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    a = [["X","O","X","O","X","O"],
         ["O","X","O","X","O","X"],
         ["X","O","X","O","X","O"],
         ["O","X","O","X","O","X"]]
    s = Solution()
    print(s.solve(a))
    print(a)
