
6 lines, Visual Explanation, O(mn)

https://leetcode.com/problems/maximal-square/discuss/61935

* Lang:    python3
* Author:  StefanPochmann
* Votes:   42

**Explanation**

What's the largest (full-of-ones-)square ending at (i,j), meaning lower right corner in row i, column j? Imagine there are 4x4 squares above, above-left and left of it:

    above  above-left  left
    
     1111     1111
     1111     1111     1111
     1111     1111     1111
     1111     1111     1111
        *         *    1111*

Clearly, if cell (i,j) itself is 1 as well, then there's a 5x5 square ending at (i,j). And if there were 5x5 squares above, above-left and left of it, then we'd have a 6x6. So to find the largest square ending at (i,j), we just take the minimum size of squares ending at (i-1,j), (i-1,j-1) and (i,j-1), and add 1.

---

**Implementation** - 164 ms

I write the maximum sizes directly into the input matrix `A`. Cell `A[i][j]` will tell the side length of the largest square ending at (i,j). I go top to bottom and left to right, so (i-1,j), (i-1,j-1) and (i,j-1) have all been handled already. First thing I do for each cell is turn it into an integer, and then if it's 1 and it's not on the top or left border of the matrix, I determine its largest-square size as explained above. In the end, I return 0 for the empty matrix and otherwise the area of the largest square ending anywhere.

    class Solution:
        def maximalSquare(self, A):
            for i in range(len(A)):
                for j in range(len(A[i])):
                    A[i][j] = int(A[i][j])
                    if A[i][j] and i and j:
                        A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
            return len(A) and max(map(max, A)) ** 2

---

**Smaller Version** - 132 ms

This version is a bit smaller and faster due to using more of Python and some "tricks":

    class Solution:
        def maximalSquare(self, A):
            for i, r in enumerate(A):
                r = A[i] = map(int, r)
                for j, c in enumerate(r):
                    if i * j * c:
                        r[j] = min(A[i-1][j], r[j-1], A[i-1][j-1]) + 1
            return max(map(max, A + [[0]])) ** 2

---

**O(n) Extra Space** - 128 ms

Here's a version that doesn't overwrite the input matrix but uses two integer lists: `s` tells the sizes of the squares ending it the current row and `p` does the same for the previous row.

    class Solution:
        def maximalSquare(self, A):
            area = 0
            if A:
                p = [0] * len(A[0])
                for row in A:
                    s = map(int, row)
                    for j, c in enumerate(s[1:], 1):
                        s[j] *= min(p[j-1], p[j], s[j-1]) + 1
                    area = max(area, max(s) ** 2)
                    p = s
            return area

Note that in Python with its integer and string objects, I'm not sure this actually saves space. But in other languages, overwriting the input array might not even be possible, and if it's possible, it might take more space than a "O(n) Extra Space" variant.
