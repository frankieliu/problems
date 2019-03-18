
Python DFS Solution, runtime 52ms and memory usage 12.6 MB

https://leetcode.com/problems/max-area-of-island/discuss/242183

* Lang:    python3
* Author:  tianqi3
* Votes:   0

Runtime: 52 ms, faster than 97.90% of Python online submissions for Max Area of Island.
Memory Usage: 12.6 MB, less than 72.22% of Python online submissions for Max Area of Island.
```
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
					# Reset cur_area to 0
                    self.cur_area = 0
                    self.dfs(grid, i, j)
                    
                    max_area = max(max_area, self.cur_area)
                    
        return max_area
        
    def dfs(self, grid, i, j):
        self.cur_area += 1
        grid[i][j] = \'#\'
        
		# Check left
        if j - 1 >= 0 and grid[i][j-1] == 1:
            self.dfs(grid, i, j-1)
        
		# Check right
        if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
            self.dfs(grid, i, j+1)
        
		# Check up
        if i - 1 >= 0 and grid[i-1][j] == 1:
            self.dfs(grid, i-1, j)
        
		# Check down
        if i + 1 < len(grid) and grid[i+1][j] == 1:
            self.dfs(grid, i+1, j)
```
