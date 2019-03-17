
O(N) 7-line Python solution, 72ms

https://leetcode.com/problems/container-with-most-water/discuss/6131

* Lang:    python3
* Author:  kitt
* Votes:   21

If `height[L] < height[R]`, move `L`, else move `R`. Say height[0] < height[5], area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than (0, 5), so no need to try them.

    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res
