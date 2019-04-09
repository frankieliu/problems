
0ms java Math

https://leetcode.com/problems/poor-pigs/discuss/239675

* Lang:    java
* Author:  monsoonwinds7
* Votes:   0

Idea is to emulate a binary search, 
number of times to search using a single pig ->  number of pigs reqired to search minutesToTest/minutesToDie  times 
```
class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
          
    return   (int) Math.round(Math.log(buckets)/Math.log(minutesToTest/minutesToDie));

    }
}
```

