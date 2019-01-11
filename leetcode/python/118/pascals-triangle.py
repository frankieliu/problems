"""118. Pascal's Triangle
Easy

543

63

Favorite

Share
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Accepted
213,978
Submissions
491,566"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows == 3:
            return [[1], [1, 1], [1, 2, 1]]

        g = self.generate(numRows - 1)
        gl = g[-1]
        nrow = [1]
        for i in range(0, len(gl)-1):
            nrow.append(gl[i] + gl[i+1])
        nrow.append(1)
        return g + [nrow]


s = Solution()
print(s.generate(5))
