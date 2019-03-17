
Easy python with explaination

https://leetcode.com/problems/range-addition-ii/discuss/103615

* Lang:    python3
* Author:  yang_fan
* Votes:   0

The key point is that, no matter how many time the **ops** add ones, the maximum numbers is just located inside the min row number **a** and min column number **b**. The solution is to simply calculate the minimum and mulptiply them to get the area.
```
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops==[]:return m*n
        min_col=ops[0][1]
        min_row=ops[0][0]
        for op in ops:
            min_row=min(min_row,op[0])
            min_col=min(min_col,op[1])
        return min_row*min_col
```
