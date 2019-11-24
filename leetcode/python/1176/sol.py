In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1176.diet-plan-performance.algorithms.json

This is confusing

https://leetcode.com/problems/diet-plan-performance/discuss/371930

* Lang:    python
* Author:  lyming90
* Votes:   28

The question coiuld be understood as looking at different segmentations. For example, given 

```
[6,13,8,7,10,1,12,11]
k = 6
lower = 5
upper = 37
```

The first 6 days would be [6, 13, 8, 7, 10, 1], the second would be [12, 11]. 

This is also how example 3 explains its solution.
