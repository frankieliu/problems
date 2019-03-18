
Golfing in Python

https://leetcode.com/problems/reverse-integer/discuss/4055

* Lang:    python3
* Author:  StefanPochmann
* Votes:   93

Get the `s`ign, get the `r`eversed absolute integer, and return their product if `r` didn't "overflow".

    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)

As compressed one-liner, for potential comparison:

    def reverse(self, x):
        s=cmp(x,0);r=int(`s*x`[::-1]);return(r<2**31)*s*r

Anybody got something shorter?
