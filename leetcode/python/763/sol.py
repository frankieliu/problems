
Python Slow way but understandable

https://leetcode.com/problems/partition-labels/discuss/243125

* Lang:    python3
* Author:  dacheng0413
* Votes:   0

```
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        num = []
        stack = []
        check = True
        while True:
            if not stack:
                stack.append(S[0])
                S=S[1:]
                continue
            if not S:
                num.append(len(stack))
                break
            for x in set(stack):
                if x in S:
                    check = False
                    break
            if not check:
                stack.append(S[0])
                S = S[1:]
            else : 
                num.append(len(stack))
                stack = []
            check = True
        return num
                
            
```
