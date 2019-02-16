"""73. Set Matrix Zeroes
Medium

827

163

Favorite

Share

Given a m x n matrix, if an element is 0, set its entire row and
column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Accepted
183,402
Submissions
474,910

"""

class Solution:
    def setZeroes(self, g):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # might as well mark one sacrificial row and column

        # but since we are using this row and column ->
        # we need to check whether the sacrificial row will zero'ed out

        m = len(g)
        n = len(g[0])

        # check for zeros in column 0
        cz = False
        for i in range(0, m):
            if g[i][0] == 0:
                cz = True
        rz = False
        for i in range(0, n):
            if g[0][i] == 0:
                rz = True

        # now we can safely override column and row 0
        for i in range(1, m):
            for j in range(1, n):
                if g[i][j] == 0:
                    g[i][0] = 0
                    g[0][j] = 0

        # now we zero out the array
        for i in range(1, m):
            if g[i][0] == 0:
                for j in range(1, n):
                    g[i][j] = 0
        for j in range(1, n):
            if g[0][j] == 0:
                for i in range(1, m):
                    g[i][j] = 0

        # now we take care of the rest
        if cz:
            for i in range(0, m):
                g[i][0] = 0
        if rz:
            for j in range(0, n):
                g[0][j] = 0


s = Solution()
a =[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

print(s.setZeroes(a))
print(a)
