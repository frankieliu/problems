
Concise Python Solution with 8 Lines

https://leetcode.com/problems/target-sum/discuss/97331

* Lang:    python3
* Author:  hweicdl
* Votes:   0

```
class Solution(object):
    def findTargetSumWays(self, nums, S):
        cacheMap = {S: 1}
        for n in nums:
            m = {}
            for target, num in cacheMap.iteritems():
                m[target+n] = m.get(target+n, 0) + num
                m[target-n] = m.get(target-n, 0) + num
            cacheMap = m
        return cacheMap.get(0, 0)
```
