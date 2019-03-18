
Python simple solution

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92996

* Lang:    python3
* Author:  wilsonsky18
* Votes:   0

Obviously, the solution is to take the difference set of two sets
```
class Solution(object):
    def findDisappearedNumbers(self, nums):
        l = set(sorted(nums))
        u = range(1,len(nums)+1)
        if len(l) > 0:
            return list(set(u) - l)
        else:
            return []
```
