
Python O(nlogn) short solution with explanation

https://leetcode.com/problems/find-right-interval/discuss/91806

* Lang:    python3
* Author:  dalwise
* Votes:   22

My solution from contest with minimal cleanup. For each end point search for the first start point that is equal or higher in a previously constructed ordered list of start points. If there is one then return its index. If not return -1:
```
def findRightInterval(self, intervals):
    l = sorted((e.start, i) for i, e in enumerate(intervals))
    res = []
    for e in intervals:
        r = bisect.bisect_left(l, (e.end,))
        res.append(l[r][1] if r < len(l) else -1)
    return res
```
