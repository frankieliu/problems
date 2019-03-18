
Short but bad Python

https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/82584

* Lang:    python3
* Author:  StefanPochmann
* Votes:   1

    def __init__(self):
        vals = set()
        self.addNum = vals.add
        self.getIntervals = lambda: [[g[0][1], g[-1][1]] for g in
                                     (list(g) for _, g in itertools.groupby(
                                      enumerate(sorted(vals)), lambda (i, val): val - i))]
