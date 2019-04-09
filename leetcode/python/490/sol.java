
Simple 9ms Java DFS (simplified & optimized alternatives)

https://leetcode.com/problems/the-maze/discuss/97100

* Lang:    java
* Author:  Shenghan-Chen
* Votes:   0

Straightforward, 13ms:
(lazy enough to not have a helper function)
```
public class Solution {
    int[][] visit;
    public boolean hasPath(int[][] maze, int[] start, int[] dest) {
        int i = start[0], j = start[1];
        if (i == dest[0] && j == dest[1]) return true;
        if (visit == null) visit = new int[row][col];
        if (visit[start[0]][start[1]]++ > 0) return false;
        int count, i1 = i, i2 = i, j1 = j, j2 = j;
        count = 0;
        while (--i1 >= 0 && maze[i1][j] != 1) count++;
        if (hasPath(maze, new int[]{i-count, j}, dest)) return true;
        count = 0;
        while (++i2 < maze.length && maze[i2][j] != 1) count++;
        if (hasPath(maze, new int[]{i+count, j}, dest)) return true;
        count = 0;
        while (--j1 >= 0 && maze[i][j1] != 1) count++;
        if (hasPath(maze, new int[]{i, j-count}, dest)) return true;
        count = 0;
        while (++j2 < maze[0].length && maze[i][j2] != 1) count++;
        if (hasPath(maze, new int[]{i, j+count}, dest)) return true;
        return false;
    }
}
```
Optimized, 9ms:
2 tricks as parallel to those from my post in [Maze II](https://discuss.leetcode.com/topic/78451/17ms-concise-java-using-bfs-with-some-variations-beats-100), 1. pre-checking; and 2. alternating vertical/horizontal direction (except for the start).
```
public class Solution {
    int row, col, count;
    boolean[][] visited;
    
    public boolean hasPath(int[][] maze, int[] start, int[] dest) {
        row = maze.length;
        col = maze[0].length;
        if (!stoppable(maze, dest[0], dest[1])) return false;
        visited = new boolean[row][col];
        return hasPath(maze, start[0], start[1], dest, 1);
    }
    
    boolean hasPath(int[][] maze, int i, int j, int[] dest, int dir) {
        if (visited[i][j]) return false;
        visited[i][j] = true;
        if (i == dest[0] && j == dest[1]) return true;
        int i1 = i, i2 = i, j1 = j, j2 = j;
        if (dir > 0) {
            count = 0;
            while (--i1 >= 0 && maze[i1][j] != 1) count++;
            if (hasPath(maze, i-count, j, dest, 0)) return true;
            count = 0;
            while (++i2 < row && maze[i2][j] != 1) count++;
            if (hasPath(maze, i+count, j, dest, 0)) return true;
        }
        if (dir < 2) {
            count = 0;
            while (--j1 >= 0 && maze[i][j1] != 1) count++;
            if (hasPath(maze, i, j-count, dest, 2)) return true;
            count = 0;
            while (++j2 < col && maze[i][j2] != 1) count++;
            if (hasPath(maze, i, j+count, dest, 2)) return true;
        }
        return false;
    }
    
    private boolean stoppable(int[][] maze, int i, int j) {
        return i == 0 || i == row-1 || j == 0 || j == col-1 || 
        maze[i-1][j] == 1 || maze[i+1][j] == 1 || maze[i][j-1] == 1 || maze[i][j+1] == 1;
    }
}
```
Oversimplified, 9ms:
(unnecessary and pretty unreadable but it just feels fun:)
```
public class Solution {
    int[][] visit;    
    public boolean hasPath(int[][] maze, int[] start, int[] dest) {
        visit = new int[maze.length][maze[0].length];
        visit[start[0]][start[1]]--;
        return hasPath(maze, start[0], start[1], dest, 0) || hasPath(maze, start[0], start[1], dest, 1);
    }
    
    boolean hasPath(int[][] maze, int i, int j, int[] dest, int x) {
        if (visit[i][j]++ > 0) return false;
        if (i == dest[0] && j == dest[1]) return true;
        int y = 1-x, c1 = 0, c2 = 0;
        while (i+c1*x >= 0 && j+c1*y >= 0 && maze[i+c1*x][j+c1*y] != 1) --c1;++c1;
        while (i+c2*x < maze.length && j+c2*y < maze[0].length && maze[i+c2*x][j+c2*y] != 1) ++c2;--c2;
        return hasPath(maze, i+c1*x, j+c1*y, dest, y) || hasPath(maze, i+c2*x, j+c2*y, dest, y);
    }
}
```
