
Java: A Bitmap beats %91, very simple

https://leetcode.com/problems/set-mismatch/discuss/105532

* Lang:    java
* Author:  tabrizi
* Votes:   0

```
public class Solution {
    public int[] findErrorNums(int[] nums) {
        int len = nums.length;
        boolean[] bitmap = new boolean[len];
        int[] results = new int[2];
        
        for ( int i = 0; i < len; i++ ) {
            int item = nums[i];
            if (bitmap[item - 1]) {
                results[0] = item;
            } else {
                bitmap[item - 1] = true;
            }
        }
        
        for ( int i = 0; i < len; i++ ) {
            if (!bitmap[i]) {
                results[1] = i+1;
            }
        }
        
        return results;
    }
}

```
