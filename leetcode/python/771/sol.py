
Python brute force

https://leetcode.com/problems/jewels-and-stones/discuss/113579

* Lang:    python3
* Author:  asyz13jinage
* Votes:   3

```
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for c in S:
            if c in J:
                count += 1
        return count
```
