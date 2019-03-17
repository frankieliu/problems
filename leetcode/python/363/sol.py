
Any Accepted Python Solution?

https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83596

* Lang:    python3
* Author:  bookshadow
* Votes:   9

I got a TLE for the Python code below, because the time cost of bisect.insort is O(n) for a built-in list.

The code was rejudged as accepted just now, but very slow... 1800ms+

    class Solution(object):
        def maxSumSubmatrix(self, matrix, k):
            """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
            m = len(matrix)
            n = len(matrix[0]) if m else 0
            
            M = max(m, n)
            N = min(m, n)
            ans = None
            for x in range(N):
                sums = [0] * M
                for y in range(x, N):
                    slist, num = [], 0
                    for z in range(M):
                        sums[z] += matrix[z][y] if m > n else matrix[y][z]
                        num += sums[z]
                        if num <= k: ans = max(ans, num)
                        i = bisect.bisect_left(slist, num - k)
                        if i != len(slist): ans = max(ans, num - slist[i])
                        bisect.insort(slist, num)
            return ans or 0

Could anybody share a more efficient Python solution? Thank you :D
