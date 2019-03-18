
Java/Python O(1) space 11 lines solution

https://leetcode.com/problems/set-matrix-zeroes/discuss/26115

* Lang:    python3
* Author:  dietpepsi
* Votes:   17

**Java**

    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length, k = 0;
        // First row has zero?
        while (k < n && matrix[0][k] != 0) ++k;
        // Use first row/column as marker, scan the matrix
        for (int i = 1; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (matrix[i][j] == 0)
                    matrix[0][j] = matrix[i][0] = 0;
        // Set the zeros
        for (int i = 1; i < m; ++i)
            for (int j = n - 1; j >= 0; --j)
                if (matrix[0][j] == 0 || matrix[i][0] == 0)
                    matrix[i][j] = 0;
        // Set the zeros for the first row
        if (k < n) Arrays.fill(matrix[0], 0);
    }

**Python**

    def setZeroes(self, matrix):
        # First row has zero?
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in xrange(1, m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in xrange(1, m):
            for j in xrange(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n
