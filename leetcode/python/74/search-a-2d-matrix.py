"""74. Search a 2D Matrix
Medium

651

81

Favorite

Share

Write an efficient algorithm that searches for a value in an m x n
matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.

The first integer of each row is greater than the last integer of the
previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
Accepted
200,311
Submissions
579,138

"""

"""

 z z z z

 y y 4 5

 x x 5 6

Say a number is less than 4 (in the position show)
What can we say?  (definitely have to be either:
1. below to the left (xx region) or (yy region)
2. or above it (zz region)

As a way to minimize the search space in y direction

t < x              t > x (cuts in half)

**********         ..........
*********x         .........x
*********.         **********
*********.         **********

the other direction

t < x              t > x (cuts in half)

********           ....****
********           ....****
***x....           ...x****


t < x         t > x

***x....     ...x****
***.....     ********
***.....     ********

Strategy:
 while t > x, keep going in the same direction (subdivide in that direction)
 but if t < x, then switch direction
"""

from itertools import chain
from bisect import bisect_left

class Solution:
    def searchMatrix(self, a, t):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        g = list(chain(*a))
        i = bisect_left(g, t)
        return g and i < len(g) and g[bisect_left(g, t)] == t or False


s = Solution()
if True:
    print(s.searchMatrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3))

    print(s.searchMatrix([
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ], 13))

    print(s.searchMatrix([
        [1]
    ], 1))

    print(s.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]], 5))

print(s.searchMatrix([[1]],2))
