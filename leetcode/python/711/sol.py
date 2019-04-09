
Use anchor and set, Python beat 100% (no sort, O(RC))

https://leetcode.com/problems/number-of-distinct-islands-ii/discuss/255021

* Lang:    python3
* Author:  sevenhe716
* Votes:   0

Many solutions use **sort** to compare island. and I speed up this process by using **anchor** and **set**.

To compare two islands. first find the anchor of islands. For example, we can choose **left_up** point as anchor.
```
offset1 = (cur_point1 - anchor1) * direction
expect_point2 = anchor2 + offset1
```
and then check whether expect_point2 is in set island2.

To support **rotation** and **reflection**, we can just change the **anchors** and **directions**, a total of eight islands:
anchors: **[left_up, right_up, left_down, right_down, up_left, up_right, down_left, down_right]**
direcitons: **[(1, 1), (1, -1), (-1, 1), (-1, -1)]**

Complexity Analysis:
Sort costs O(nlogn), in compare, find anchor costs O(n), check whether point in set costs n * O(1). 
Decrease the total time complexity from O(RClog(RC)) to O(RC), space complexity remains O(RC)

    def numDistinctIslands2(self, grid: \'List[List[int]]\') -> int:
        if not grid:
            return 0
        m, n, islands = len(grid), len(grid[0]), []
        dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        def dfs(i, j, island):
            island.add((i, j))
            grid[i][j] = 0
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                dfs(i - 1, j, island)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                dfs(i, j - 1, island)
            if i + 1 < m and grid[i + 1][j] == 1:
                dfs(i + 1, j, island)
            if j + 1 < n and grid[i][j + 1] == 1:
                dfs(i, j + 1, island)

        def check_unique(anchor1, anchor2, dir, island, cur_island, reverse):
            for pos in island:
                offset = ((pos[0] - anchor1[0]) * dir[0], (pos[1] - anchor1[1]) * dir[1])
                if reverse:
                    pos2 = (offset[1] + anchor2[0], offset[0] + anchor2[1])
                else:
                    pos2 = (offset[0] + anchor2[0], offset[1] + anchor2[1])

                if pos2 not in cur_island:
                    return True
            return False

        def check_uniques(island):
            anchors1, anchors2 = [], []
            for dir in dirs:
                anchors1.append(min(island, key=lambda x: (x[0] * dir[0], x[1] * dir[1])))
                anchors2.append(min(island, key=lambda x: (x[1] * dir[1], x[0] * dir[0])))

            for cur_island in islands:
                if len(cur_island) != len(island):
                    continue

                cur_anchor = min(cur_island, key=lambda x: (x[0], x[1]))
                for dir, anchor1, anchor2 in zip(dirs, anchors1, anchors2):
                    if not check_unique(anchor1, cur_anchor, dir, island, cur_island, False):
                        return False
                    if not check_unique(anchor2, cur_anchor, dir, island, cur_island, True):
                        return False
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = set()
                    dfs(i, j, island)
                    if check_uniques(island):
                        islands.append(island)
        return len(islands)
