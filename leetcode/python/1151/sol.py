In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1151.minimum-swaps-to-group-all-1s-together.algorithms.json

[Java]Sliding window O(n) with detailed explanation, very easy to understand

https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/discuss/355506

* Lang:    python
* Author:  eecandy
* Votes:   8

Thinking about it:  **the final result we want is a window with length of n** (total number of the 1s)
Check all the window with the same length n, **find the maximum one which already contains the most 1s.**
All we need to do is to swap the rest:  n-max.

```
class Solution {
    public int minSwaps(int[] nums) {
        if(nums.length < 3) return 0;
        int n = 0;
        for(int num: nums){
            if(num == 1) n++; // total number of 1s
        }
        int i=0, j=0, c=0, max=0; //sliding window i to j
        while(j < nums.length) {
            while(j < nums.length && j - i < n){ //until i to j == n or search is done
                if(nums[j++] == 1) c++;
            }
            max = Math.max(c, max); // max all the sliding window of which length equals to n
            if(j == nums.length) break;
            
            if(nums[i++] == 1) { //move i forward
                c--;
            }
        }
        return n - max; //this is the minimun swaps  
    }
}
```
