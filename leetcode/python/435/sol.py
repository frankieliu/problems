
Python short (8 lines) greedy solution with explanation

https://leetcode.com/problems/non-overlapping-intervals/discuss/91785

* Lang:    python3
* Author:  dalwise
* Votes:   2

My solution from the contest with minimal cleanup. Iterate through sorted intervals. If two successive intervals overlap then we must eliminate one, so we increase the result. The new lo interval to consider will be the old hi one, unless the old lo and hi overlap partially (the lo only covers part of the high). The lo interval will be changed to the high one if:

* The lo & hi intervals don't overlap, so we continue checking the following intervals
* The lo interval completely covers the hi one, then the lo is a better candidate to remove

```
def eraseOverlapIntervals(self, intervals):
    intervals.sort(key=operator.attrgetter('start', 'end'))
    res = lo = 0
    for hi in range(1, len(intervals)):
        if intervals[lo].end > intervals[hi].start:
            res += 1
        if not intervals[hi].start < intervals[lo].end < intervals[hi].end:
            lo = hi
    return res
```
