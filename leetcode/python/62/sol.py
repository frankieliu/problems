
1 Line Math Solution (Python)

https://leetcode.com/problems/unique-paths/discuss/23003

* Lang:    python3
* Author:  gavy
* Votes:   29

    class Solution(object):
        def uniquePaths(self, m, n):
            """
            :type m: int
            :type n: int
            :rtype: int
            """
            return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)
