
Can someone tell me how to improve the code?

https://leetcode.com/problems/self-dividing-numbers/discuss/237830

* Lang:    python3
* Author:  jeffwzhong
* Votes:   0

```
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            res.append(self.is_selfdividingnum(i))
        res = filter(None, res)
        return res
    
    def is_selfdividingnum(self,n):
        t = n
        rec = []
        s = 0
        while n:
            rec.append(n%10)
            n //= 10

        for i in rec:
            print(t)
            if i == 0:
                break
            s += t % i
        if i!= 0 and s == 0:
            return t
```
