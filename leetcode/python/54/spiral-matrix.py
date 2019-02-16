"""54. Spiral Matrix
Medium

825

330

Favorite

Share

Given a matrix of m x n elements (m rows, n columns), return all
elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Accepted
196,542
Submissions
674,941

"""

class Solution:
    def top(self, out, m, offx, offy):
        i = offx
        j = offy
        while j < (len(m[0]) - offy):
            out.append(m[i][j])
            j += 1
        return(out)

    def right(self, out, m, offx, offy):
        i = offx + 1
        if len(m[0]) - offy - 1 >= offy:
            while i < (len(m) - offx):
                out.append(m[i][len(m[0])-offy-1])
                i += 1
        return(out)

    def bottom(self, out, m, offx, offy):
        j = len(m[0]) - offy - 2
        if len(m) - offx - 1 != offx:
            while j >= offy:
                out.append(m[len(m)-offx-1][j])
                j -= 1
        return(out)

    def left(self, out, m, offx, offy):
        i = len(m) - offx - 2
        if len(m[0]) - offy - 1 != offy:
            while i > offx:
                out.append(m[i][offy])
                i -= 1
        return(out)

    def spiralOrder(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if len(m) == 0:
            return []

        offx = 0
        offy = 0
        sn = len(m)
        sm = len(m[0])

        out = []
        while sn > 0 and sm > 0:
            offx = (len(m) - sn) // 2
            offy = (len(m[0]) - sm) // 2
            self.top(out, m, offx, offy)
            self.right(out, m, offx, offy)
            self.bottom(out, m, offx, offy)
            self.left(out, m, offx, offy)
            sn -= 2
            sm -= 2

        return(out)


s = Solution()

print(s.spiralOrder(
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]))

print(s.spiralOrder(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]))

print(s.spiralOrder(
    [
        [6, 7]
    ]))

print(s.spiralOrder(
    [
        [6],
        [7],
        [8],
        [9]
    ]))
print(s.spiralOrder(
    [
        [6]
    ]))
