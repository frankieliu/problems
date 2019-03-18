
Python beats 99.95%

https://leetcode.com/problems/robot-return-to-origin/discuss/236131

* Lang:    python3
* Author:  jeffwzhong
* Votes:   0

```
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u = moves.count(\'U\')
        d = moves.count(\'D\')
        l = moves.count(\'L\')
        r = moves.count(\'R\')

        if (u - d) == 0 and (l -r) == 0:
            return True
        else:
            return False
```
Easy.
