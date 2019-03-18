
Python 16ms ASCII

https://leetcode.com/problems/to-lower-case/discuss/237482

* Lang:    python3
* Author:  dacheng0413
* Votes:   1

```
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        stack = [ord(x) for x in str]
        for i in range(len(stack)):
            if stack[i] > 64 and stack[i] < 91:
                stack[i] += 32
        asw=[chr(x) for x in stack]
        
        return \'\'.join(asw)
		```
