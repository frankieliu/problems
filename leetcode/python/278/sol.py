
Python, understand (easily from Binary search idea)

https://leetcode.com/problems/first-bad-version/discuss/71324

* Lang:    python3
* Author:  weizhi2
* Votes:   19

    class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n-1
        l = 0
        while(l<=r):
            mid = l + (r-l)/2
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l
