
Simple java dfs solution

https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90828

* Lang:    java
* Author:  yzj1212
* Votes:   3

Build two sets for Pacific and Atlantic. The result is the intersection of them.
```
 private int[][] direction = new int[][]{{1, 0},{0, 1},{-1, 0},{0, -1}};
    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> result = new ArrayList<>();
        if (matrix.length == 0) return result;
        Set<Integer> pacific = new HashSet<>();
        Set<Integer> atlantic = new HashSet<>();
        for (int i = 0; i < matrix[0].length; i++) {
            dfs(matrix, 0, i, pacific);
            dfs(matrix, matrix.length - 1, i, atlantic);
        }
        for (int i = 0; i < matrix.length; i++) {
            dfs(matrix, i, 0, pacific);
            dfs(matrix, i, matrix[0].length - 1, atlantic);
        }
        
        for (int i: pacific) {
            if (atlantic.contains(i)) {
                result.add(decode(i, matrix));
            }
        }
        return result;
    }
    
    private void dfs(int[][] matrix, int i, int j, Set<Integer> result) {
        if (!result.add(encode(i, j, matrix))) return;
        for (int[] dir: direction) {
            int x = dir[0] + i;
            int y = dir[1] + j;
            if (x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length && matrix[x][y] >= matrix[i][j]) {
                dfs(matrix, x, y, result);
            }
        }
    }
    
    private int[] decode(int i, int[][] matrix) {
        return new int[]{i / matrix[0].length, i % matrix[0].length};
    }
    
    private int encode(int i, int j, int[][] matrix) {
        return i * matrix[0].length + j;
    }
```
