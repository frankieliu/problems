"""48. Rotate Image
Medium

1176

110

Favorite

Share
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
Accepted
211,575
Submissions
462,222"""

class Solution:
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # 0,0 0,1 0,2 0,3 0,4 0,5
        #        --------------->
        # 1,0   ^ 1,1 1,2 1,3 1,4 |  1,5
        # 2,0   | 2,1 2,2 2,3 2,4 |  2,5
        # 3,0   | 3,1 3,2 3,3 3,4 |  3,5
        # 4,0   | 4,1 4,2 4,3 4,4 v
        #         <--------------
        # 5,0     5,1

        #   from i = 0 to 5//2:
        #     from j = 0, n-i-1
        #
        #   (i,i)   -> (i,n-i)    -> (n-i,n-i)   -> (n-i,i)
        #   (i,i+j) -> (i+j, n-i) -> (n-i,n-i-j) -> (n-i-j,i)

        # pvatala@gmail.com

        n = len(m)
        for i in range(0, n//2):
            for j in range(0, n-2*i-1):
                (m[i+j][n-i-1],
                 m[n-i-1][n-i-1-j],
                 m[n-i-1-j][i],
                 m[i][i+j]) = (
                    m[i][i+j],
                    m[i+j][n-i-1],
                    m[n-i-1][n-i-1-j],
                    m[n-i-1-j][i]
                )



s = Solution()
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

s.rotate(m)
print(m)
