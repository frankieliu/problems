
Recursive solution in Python

https://leetcode.com/problems/remove-k-digits/discuss/88720

* Lang:    python3
* Author:  ra1den
* Votes:   0

We just need to make sure in each step the *num* becomes smaller. 

* It's prior to remove the leading zeros within k steps if possible. 
* Otherwise remove last digit of num's ascending prefix.

I suppose time complexity is O(nk)
```
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if not num or len(num) == k:
            return "0"
        if k == 0:
            return num
        idx = num.find('0')
        if 0 <= idx <= k:
            return self.removeKdigits(num[idx+1:], k - idx)
        for i in range(1,len(num)):
            if num[i] < num[i-1]:
                return self.removeKdigits(num[:i-1]+num[i:], k-1)
        return num[:-k]
```
