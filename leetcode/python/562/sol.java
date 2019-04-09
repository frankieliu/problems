
Java O(1) Space and O(mn) Time, 69% Running Time Percentile

https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/discuss/102273

* Lang:    java
* Author:  y5yeyey
* Votes:   1

```java


class Solution {
    public int maxLine(int[][] M, int m, int n, int i, int j, int x, int y) {
        if (i < 0 || i >= m || j < 0 || j >= n || M[i][j] == 0) {
            return 0;
        }
        // visited: ver-2, hor-3, di-5, andi-7
        // if visits both ver and hor, then M[i][j] = 6
        // ver
        if (x == 0 && M[i][j] % 2 != 0) {
            M[i][j] *= 2;
            return 1 + maxLine(M, m, n, i+x, j+y, x, y);
        }
        // hor 
        if (y == 0 && M[i][j] % 3 != 0) {
            M[i][j] *= 3;
            return 1 + maxLine(M, m, n, i+x, j+y, x, y);
        }
        // di
        if (x == y && M[i][j] % 5 != 0) {
            M[i][j] *= 5;
            return 1 + maxLine(M, m, n, i+x, j+y, x, y);
        }
        // andi
        if (x == -y && M[i][j] % 7 != 0) {
            M[i][j] *= 7;
            return 1 + maxLine(M, m, n, i+x, j+y, x, y);
        }
        return 0;
    }
    public int longestLine(int[][] M) {
        if (M.length == 0 || M[0].length == 0) {
            return 0;
        }
        int m = M.length;
        int n = M[0].length;
        int res = 0;
        int ver, hor, di, andi;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (M[i][j] > 0) {
                    ver = maxLine(M, m, n, i, j, 0, 1);
                    hor = maxLine(M, m, n, i, j, 1, 0);
                    di = maxLine(M, m, n, i, j, 1, 1);
                    andi = maxLine(M, m, n, i, j, 1, -1);
                    res = Math.max(res, Math.max(Math.max(di, andi), Math.max(ver, hor)) );
                }
            }
        }
        return res;
    }
}
```
