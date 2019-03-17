
python long solution

https://leetcode.com/problems/island-perimeter/discuss/255370

* Lang:    python3
* Author:  aptxj
* Votes:   0

```
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ht = {}
        
        width = len(grid[0])
        height = len(grid)
        
        # add lakes around the grid
        for h in range(height):
            grid[h].insert(0, 0)
            grid[h].append(0)
        
        grid.insert(0, [0]*(width+2))
        grid.append([0]*(width+2))
        
        res = 0
        for h in range(1, height+1):
            for w in range(1, width + 1):
                if grid[h][w] == 1:
                    res += 4 + -1 * (grid[h-1][w] + grid[h+1][w] + grid[h][w-1] + grid[h][w+1])
        return res
```
