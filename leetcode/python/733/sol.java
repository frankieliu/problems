
Java 7ms 100% faster (recursive)

https://leetcode.com/problems/flood-fill/discuss/255483

* Lang:    java
* Author:  kbenriquez
* Votes:   0

```
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int[][] visited = new int[image.length][image[0].length];
        fill(image, visited, sr, sc, newColor, image[sr][sc]);
        return image;
    }
    
    public void fill(int[][] image, int[][] visited, int row, int col, int color, int startingColor){
        if(row < 0 || row >= image.length 
           || col < 0 || col >= image[row].length 
           || visited[row][col] == 1 
           || image[row][col] == color
           || image[row][col] != startingColor)
            return;
        image[row][col] = color; /*change to new color*/
        visited[row][col] = 1; /*mark as visited*/
        
        fill(image, visited, row-1, col, color, startingColor); /*check top*/
        fill(image, visited, row, col-1, color, startingColor); /*check left*/
        fill(image, visited, row, col+1, color, startingColor); /*check right*/
        fill(image, visited, row+1, col, color, startingColor); /*check bottom*/
    }
}
```
