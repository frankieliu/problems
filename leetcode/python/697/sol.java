
Easiest One Pass Java Solution, Beats 100%

https://leetcode.com/problems/degree-of-an-array/discuss/108659

* Lang:    java
* Author:  SanD91
* Votes:   0

Create a static class to hold a number's start, end and degree info. Use that to find the max degree and min count; Map is used for fast lookup.

```
class Solution {
    static class Num {
        int num;
        int start;
        int end;
        int degree;
        
        public Num(int num, int index) {
            this.num = num;
            this.start = index;
            this.end = index;
            this.degree = 1;
        }
    }
    
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Num> map = new HashMap<>();
        int degree = 0, count = Integer.MAX_VALUE, curCount = 0, value = 0;
        Num cur = null;
        
        for(int i = 0; i < nums.length; ++i) {
            value = nums[i];
            if(!map.containsKey(value)) {
                cur = new Num(value, i);
                map.put(value, cur);
            } else {
                cur = map.get(value);
                cur.degree++;
                cur.end = i;
            }
            
            if(cur.degree > degree) {
                degree = cur.degree;
                count = cur.end - cur.start + 1;
            } else if(cur.degree == degree && count > (cur.end - cur.start + 1)) {
                count = cur.end - cur.start + 1;
            }
        }
        return count;
    }
}
```
