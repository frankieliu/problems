
Python game of life like solution

https://leetcode.com/problems/rotting-oranges/discuss/240169

* Lang:    python3
* Author:  jorgechato
* Votes:   0

Runtime: **92** ms, faster than **100.00%** of Python3 online submissions for Rotting Oranges.
Memory Usage: **12.4** MB

```
class Solution:
    """
    Input: 1 array[array[int]]. grid (array[array[int]])
    Output: 1 int. number of minutes (whether all oranges take to
    collapse)
    Constrains:
        - 1 <= grid.length <= 10
        - 1 <= grid[0].length <= 10
        - grid[i][j] is only 0, 1, or 2.
    Edge Cases:

    Time complexity: O(N\u02C62*M)
    """
    def orangesRotting(self, grid: \'List[List[int]]\') -> \'int\':
        minutes = 0
        changed = True

        while changed:
            grid, changed = self.next_grid(grid)

            if changed:
                minutes += 1

        return -1 if any(1 in row for row in grid) else minutes

    def next_grid(self, grid):
        changed = 0
        new_grid = [x[:] for x in grid]

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                cell = 2 if self.should_die(x, y, grid) else grid[x][y]
                changed += 1 if cell != grid[x][y] else 0
                new_grid[x][y] = cell
        
        return new_grid, False if changed == 0 else True

    def should_die(self, x, y, grid):
        v_neighbours = [self.get(x-1, y, grid), self.get(x+1, y, grid)]
        h_neighbours = [self.get(x, y-1, grid), self.get(x, y+1, grid)]
        
        total_neighbours = h_neighbours + v_neighbours

        return False if not 2 in total_neighbours or grid[x][y] == 0 else True

    def get(self, x, y, grid):
        return 0 if x >= len(grid) or y >= len(grid[x]) or y<0 or x<0 else grid[x][y]
```
