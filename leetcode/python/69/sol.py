
Python binary search solution (O(lgn)).

https://leetcode.com/problems/sqrtx/discuss/25061

* Lang:    python3
* Author:  caikehe
* Votes:   31

        
    # Binary search  
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1
