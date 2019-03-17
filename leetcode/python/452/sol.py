
Python beats 100% , easy to understand

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/256088

* Lang:    python3
* Author:  qaref18
* Votes:   0

```
def findMinArrowShots(self, points):
        if len(points) == 0:
            return 0 
        points = sorted(points, key=lambda x:x[1])
        arrowLastHit = -float(\'inf\')
        arrow = 0
        for each in points:
            if each[0] > arrowLastHit:
                arrow += 1
                arrowLastHit = each[1]
        return arrow

