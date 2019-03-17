
1 line python solution

https://leetcode.com/problems/power-of-two/discuss/64110

* Lang:    python3
* Author:  shuiyuan
* Votes:   16

    def isPowerOfTwo(self, n):
        return (n>0) and (n & (n-1))==0
