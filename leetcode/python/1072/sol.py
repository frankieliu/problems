In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1072.flip-columns-for-maximum-number-of-equal-rows.algorithms.json

Java easy solution + explanation

https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/discuss/303897

* Lang:    python
* Author:  motorix
* Votes:   48

Assume the ```i-th``` row is an all-0s row after flipping ```x``` columns.
1. If there are any other all-0s row, say ```j-th``` row, then the ```j-th``` row before flipping should be the same as the ```i-th``` row.
2. If there are any other all-1s row, say ```k-th``` row, then the ```k-th``` row before flipping should be totally different from the ```i-th``` row.

For example:	
```
 [1,0,0,1,0]                                      [0,0,0,0,0]  // all-0s
 [1,0,0,1,0]  after flipping 0-th and 4-th rows   [0,0,0,0,0]  // all-0s
 [1,0,1,1,1] -----------------------------------> [0,0,1,0,1]
 [0,1,1,0,1]                                      [1,1,1,1,1]  // all-1s
 [1,0,0,1,1]                                      [0,0,0,0,1]
 
 1st, 2nd, and 4th rows have all values equal.
```
After flipping, the 1st and 2nd rows are all-0s, and the 4th row are all-1s. We can find that before flipping:
    the 2nd row is the same as the 1st row.
    the 4th row is totally different from the 1st row.

So, the problem is transformed to: **Find the i-th row, which has the most same or totaly different rows in the matrix.**

--

Java:
```
class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        int ans = 0;
        int m = matrix.length, n = matrix[0].length;
        int[] flip = new int[n];
        for(int i = 0; i < m; i++) {
            int cnt = 0;
            for(int j = 0; j < n; j++) flip[j] = 1 - matrix[i][j];
            for(int k = 0; k < m; k++) {
                if(Arrays.equals(matrix[k], matrix[i]) || Arrays.equals(matrix[k], flip)) cnt++;
            }
            ans = Math.max(ans, cnt);
        }
        return ans;
    }
}
```
