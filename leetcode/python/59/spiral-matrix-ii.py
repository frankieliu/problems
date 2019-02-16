"""59. Spiral Matrix II
Medium

355

69

Favorite

Share
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

import math

class Solution:

    def right(self, dir):
        if dir == [0, 1]:
            return [1, 0]
        if dir == [1, 0]:
            return [0, -1]
        if dir == [0, -1]:
            return [-1, 0]
        if dir == [-1, 0]:
            return [0, 1]

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]

        s = n
        out = [0] * s
        for i in range(0, s):
            out[i] = [None] * s
        dir = [0, 1]
        i, j = 0, -1
        for k in range(1, s**2+1):
            ni, nj = i + dir[0], j + dir[1]
            while ni == s or nj == s or out[ni][nj] is not None:
                dir = self.right(dir)
                ni, nj = i + dir[0], j + dir[1]
            # print(i, j, ni, nj, s)
            i, j = ni, nj
            out[i][j] = k

        return out


s = Solution()
# print(s.generateMatrix(1**2))
# print(s.generateMatrix(2**2))
# print(s.generateMatrix(3**2))
# print(s.generateMatrix(4**2))
# print(s.generateMatrix(5**2))
# print(s.generateMatrix(6**2))
print(s.generateMatrix(3))
