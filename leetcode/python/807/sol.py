
Python 24ms Code

https://leetcode.com/problems/max-increase-to-keep-city-skyline/discuss/237413

* Lang:    python3
* Author:  dacheng0413
* Votes:   1

```
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top_max=[]
        left_max=[]
        for i in range(len(grid)):
            left_max.append(max(grid[i]))
        for i in range(len(grid[0])):
            top_max.append(max(item[i] for item in grid))
        result = 0
        for i in range(len(top_max)):
            for j in range(len(left_max)):
                if top_max[i] < left_max[j]:
                    result += top_max[i] - grid[i][j]
                else:
                    result += left_max[j] - grid[i][j]
        return result
	```
