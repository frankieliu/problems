
Java constant space solution, space O(1), time O(n)

https://leetcode.com/problems/arithmetic-slices/discuss/90146

* Lang:    java
* Author:  MadDetective
* Votes:   0

Constant space & one pass.
Space: O(1)
Time: O(n)
```
public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        if(A==null || A.length<3) return 0;
        int res = 0, k=0;
        for(int i=1; i<A.length;i++){
            k = getArithmeticSlices(i, A[i]-A[i-1], A);
            res += (k+1)*k/2;
            i += k;
        }
        return res;
    }
    //return length of the Arithmetic slices start from s-1, s, ... 
    private int getArithmeticSlices(int s, int diff, int[] A){
        int len = 0;
        for(int i=s+1; i<A.length; i++){
            if(A[i]-A[i-1] == diff){
                len++;
            } else break;
        }
        return len;
    }
}
```
