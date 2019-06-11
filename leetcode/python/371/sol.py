
Python Solution

https://leetcode.com/problems/sum-of-two-integers/discuss/84410

* Lang:    python3
* Author:  bookshadow
* Votes:   10

Python code as follows:
```
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
```