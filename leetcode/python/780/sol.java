
[Java] Easy to understand recursion solution

https://leetcode.com/problems/reaching-points/discuss/114728

* Lang:    java
* Author:  gges5110
* Votes:   6

```
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        if (sx == tx && sy == ty) {
            return true;
        } else if (tx == ty || sx > tx || sy > ty) { 
            return false;
        } else if (tx > ty) {
            int subtract = Math.max(1, (tx - sx)/ty);
            return reachingPoints(sx, sy, tx - subtract * ty, ty);                 
        } else {
            int subtract = Math.max(1, (ty - sy)/tx);
            return reachingPoints(sx, sy, tx, ty - subtract * tx);
        }
    }
}
```
