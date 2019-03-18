
My easy python solution

https://leetcode.com/problems/arranging-coins/discuss/92301

* Lang:    python3
* Author:  yang_fan
* Votes:   0

The idea is to find the rule of the samples.
```
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        if n==1:return 1
        while(n>=i):
            n=n-i
            i+=1
        return (i-1)
```
