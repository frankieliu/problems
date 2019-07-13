In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1067.digit-count-in-range.algorithms.json

Simple iterative Java solution extending [number of digits one]

https://leetcode.com/problems/digit-count-in-range/discuss/303462

* Lang:    python
* Author:  liyun1988
* Votes:   14

The solution is based on https://leetcode.com/articles/number-of-digit-one/. Huge Kudos to the origional author of that article. 

My solution extends that solution in two places.
1 when d > 0, the remainder should be larger than i * d instead of i;
2 when d == 0, when analyzing the remainder, we need avoid taking numbers with "heading zero" like 0xxxx into the total count.

```
class Solution {
    public int digitsCount(int d, int low, int high) {
        return countDigit(high, d) - countDigit(low-1, d);
    }
    
    int countDigit(int n, int d) {
        if(n < 0 || n < d) {
            return 0;
        }
        
        int count = 0;
        for(long i = 1; i <= n; i*= 10) {
            long divider = i * 10;
            count += (n / divider) * i;
            
            if (d > 0) {
                count += Math.min(Math.max(n % divider - d * i + 1, 0), i); // comment1: tailing number need to be large than d *  i to qualify.
            } else {
                if(n / divider > 0) {
                    if(i > 1) {  // comment2: when d == 0, we need avoid to take numbers like 0xxxx into account.
                        count -= i;
                        count += Math.min(n % divider + 1, i);  
                    }
                }
            }
        }
        
        return count;
    }
}
```
