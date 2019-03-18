
Python AC with 63ms, 3lines

https://leetcode.com/problems/reverse-bits/discuss/54740

* Lang:    python3
* Author:  jaly50
* Votes:   33

    class Solution:
        # @param n, an integer
        # @return an integer
        def reverseBits(self, n):
            oribin='{0:032b}'.format(n)
            reversebin=oribin[::-1]
            return int(reversebin,2)
