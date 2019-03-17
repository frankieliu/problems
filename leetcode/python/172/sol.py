
My python solution in O(1) space O(logN) time

https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52399

* Lang:    python3
* Author:  joe1234wu
* Votes:   17

**Concept:**

Since 0 only company with 5*2
So only need to count the volume of 5 factor. (because 2 always enough)

So..
100! 's  zero has => floor(100/5) + floor(100/25) =  floor(100/5) + floor((100/5)/5) 

**Code:**

    class Solution(object):
        def trailingZeroes(self, n):
            zeroCnt = 0
            while n > 0:
                n = n/5; zeroCnt += n
            
            return zeroCnt
