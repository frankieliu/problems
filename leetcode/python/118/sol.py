
Simple Python 4 lines

https://leetcode.com/problems/pascals-triangle/discuss/38277

* Lang:    python3
* Author:  girikuncoro
* Votes:   39

    def generate(numRows):
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
