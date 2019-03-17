
Python Two Lines Simple & Clear Solution

https://leetcode.com/problems/binary-number-with-alternating-bits/discuss/112656

* Lang:    python3
* Author:  fuxuemingzhu
* Votes:   0

Two near number in binary `n` should be different. So I get this very simple and clear solution.
```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n = bin(n)[2:]
        return all(bin_n[i] != bin_n[i+1] for i in xrange(len(bin_n) - 1))
```
