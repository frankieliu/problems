In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1030.matrix-cells-in-distance-order.algorithms.json

O(N) Java BFS

https://leetcode.com/problems/matrix-cells-in-distance-order/discuss/278843

* Lang:    python
* Author:  _topspeed_
* Votes:   31

```
public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
    boolean[][] visited = new boolean[R][C];
    int[][] result = new int[R * C][2];
    int i = 0;
    Queue<int[]> queue = new LinkedList<int[]>();
    queue.offer(new int[]{r0, c0});
    while (!queue.isEmpty()) {
      int[] cell = queue.poll();
      int r = cell[0];
      int c = cell[1];

      if (r < 0 || r >= R || c < 0 || c >= C) {
        continue;
      }
      if (visited[r][c]) {
        continue;
      }

      result[i] = cell;
      i++;
      visited[r][c] = true;

      queue.offer(new int[]{r, c - 1});
      queue.offer(new int[]{r, c + 1});
      queue.offer(new int[]{r - 1, c});
      queue.offer(new int[]{r + 1, c});
    }
    return result;
  }
  ```
