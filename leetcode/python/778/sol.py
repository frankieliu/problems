
DP Python 443ms

https://leetcode.com/problems/swim-in-rising-water/discuss/113761

* Lang:    python3
* Author:  Root7
* Votes:   2

I am new to the algrithom. My first try to post for the hard. 
Basically, my thought is finding the minimum steps to reach the right bottom first. It would be at least max(2N-2, grid[-1][-1]). Then use dfs to check if it is possible to reach the end. 
Feel free to leave any comments. I am sure there is a better solution. 
```
class Solution(object):
    def swimInWater(self, grid):
        m = len(grid)
        l, r = 2*m-2, m*m 
        
        def search(i,j):
            if ele[i][j]:
                return False
            ele[i][j] = 1
            if grid[i][j] <= ans:
                if i == j == m-1:
                    return True
                return any([search(a,b) for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] 
                                                     if 0 <= a < m and 0 <= b < m])
                               
        for ans in range(max(l,grid[-1][-1]), r):
            ele = [[0] * m for _ in range(m)]
            if search(0, 0):
                return ans
```
