
Easy-to-understand python solution

https://leetcode.com/problems/number-complement/discuss/96071

* Lang:    python3
* Author:  PeterWu
* Votes:   1

```
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        complement = 0
        digit = 0
        while num > 0:
            if num % 2 == 0:
                complement += 2 ** digit
            digit += 1
            num >>= 1
        return complement
```
