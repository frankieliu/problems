
Java 1ms, 100% faster

https://leetcode.com/problems/rectangle-overlap/discuss/258649

* Lang:    java
* Author:  kbenriquez
* Votes:   0

This solution checks the positions of the points by axis. First if statement checks where the rectangles are on the x-axis and find the higher and lower rectangles and checks if there is an overlap.
For example, if the first `if` statement and the `if` statement inside it are satisfied, that means rec1 is the left and lower rectangle so an overlap only happens if `rec1[2]` and `rec1[3]` are greater than `rec2[2] `and `rec2[3]`.
```
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        if(rec1[0] < rec2[0]){
            if(rec1[1] < rec2[1])
                return rec1[2] > rec2[0] && rec1[3] > rec2[1];
            else
                return rec1[2] > rec2[0] && rec1[1] < rec2[3];
        }
        else{
            if(rec2[1] < rec1[1])
                return rec2[2] > rec1[0] && rec2[3] > rec1[1];
            else
                return rec2[2] > rec1[0] && rec2[1] < rec1[3];
        }
    }
}
```
