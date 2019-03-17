
7 lines, easy, Python

https://leetcode.com/problems/merge-intervals/discuss/21227

* Lang:    python3
* Author:  StefanPochmann
* Votes:   164

Just go through the intervals sorted by start coordinate and either combine the current interval with the previous one if they overlap, or add it to the output by itself if they don't.

    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out
