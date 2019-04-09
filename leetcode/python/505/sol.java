
17ms concise Java using BFS, with some variations (beats 100%)

https://leetcode.com/problems/the-maze-ii/discuss/98445

* Lang:    java
* Author:  Shenghan-Chen
* Votes:   0

To save the trouble of creating extra class, a little trick is to represent (i, j, l) as one integer (l*row+i)*col+j when added to PriorityQueue, which preserves the ordering w.r.t. path length l.
```
public class Solution {
    int row, col, size;
    int[][] dis; //record min distance to reach a cell from start
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        row = maze.length;
        if (row == 0) return -1;
        col = maze[0].length;
        size = row*col;
        dis = new int[row][col];
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        offer(pq, 0, start[0], start[1]);
        while (!pq.isEmpty()) {
            int t = pq.poll();
            int l = t/size, i = t%size/col, j = t%size%col; //the little trick; or replace it with an object for clarity

            if (i == destination[0] && j == destination[1]) return l; //since head of pq has smallest l, we're done
            int count = 0;
            int i1 = i, i2 = i, j1 = j, j2 = j;
            while (--i1 >= 0 && maze[i1][j] != 1) count++;
            if (count > 0) offer(pq, l+count, i-count, j);
            count = 0;
            while (++i2 < row && maze[i2][j] != 1) count++;
            if (count > 0) offer(pq, l+count, i+count, j);
            count = 0;
            while (--j1 >= 0 && maze[i][j1] != 1) count++;
            if (count > 0) offer(pq, l+count, i, j-count);
            count = 0;
            while (++j2 < col && maze[i][j2] != 1) count++;
            if (count > 0) offer(pq, l+count, i, j+count);
        }
        return -1;
    }
    
    // enqueue if unvisited or path shorter than previous
    private void offer(PriorityQueue<Integer> pq, int l, int i, int j) {
        if (dis[i][j] == 0 || dis[i][j] > l) {
            dis[i][j] = l;
            pq.offer(l*size+i*col+j);
        }
    }
}

```
Below are two optimizations (that didn't actually result in faster runtime). First is to check whether ball would ever stop at destination, i.e. whether dest. cell "floats in the air". Second is to remember the direction from which a cell is reached (horizontal or vertical), and from this spot only move along the other axis (vertical or horizontal, respectively).
```
public class Solution {    
    int row, col, size;
    int[][] dis;
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        row = maze.length;
        if (row == 0) return -1;
        col = maze[0].length;
        if (!stoppable(maze, destination[0], destination[1])) return -1;// pre-check
        size = row*col;
        dis = new int[row][col];
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        offer(pq, 0, start[0], start[1], 0);
        offer(pq, 0, start[0], start[1], 1);
        while (!pq.isEmpty()) {
            int t = pq.poll();
            int d = 1-t%3, l = t/3/size, i = t/3%size/col, j = t/3%size%col;
            if (i == destination[0] && j == destination[1]) return l;
            int count = 0;
            if (d == 0) {
                int i1 = i, i2 = i;
                while (--i1 >= 0 && maze[i1][j] != 1) count++;
                if (count > 0) offer(pq, l+count, i-count, j, d);
                count = 0;
                while (++i2 < row && maze[i2][j] != 1) count++;
                if (count > 0) offer(pq, l+count, i+count, j, d);
                continue;
            }
            int j1 = j, j2 = j;
            while (--j1 >= 0 && maze[i][j1] != 1) count++;
            if (count > 0) offer(pq, l+count, i, j-count, d);
            count = 0;
            while (++j2 < col && maze[i][j2] != 1) count++;
            if (count > 0) offer(pq, l+count, i, j+count, d);
        }
        return -1;
    }
    
    private void offer(PriorityQueue<Integer> pq, int l, int i, int j, int d) {
        if (dis[i][j] == 0 || dis[i][j] > l) {
            dis[i][j] = l;
            pq.offer((l*size+i*col+j)*3+d);
        }
    }
    
    private boolean stoppable(int[][] maze, int i, int j) {
        return i == 0 || i == row-1 || j == 0 || j == col-1 || 
        maze[i-1][j] == 1 || maze[i+1][j] == 1 || maze[i][j-1] == 1 || maze[i][j+1] == 1;
    }
}
```
