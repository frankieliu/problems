
Python Easy-to-understand Solution

https://leetcode.com/problems/utf-8-validation/discuss/87530

* Lang:    python3
* Author:  jason-junchen
* Votes:   0

```
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return False
        
        i, n = 0, len(data)
        arr = [bin(x)[2:].rjust(8, '0') for x in data]
        while i < n:
            cnt = len(arr[i]) - len(arr[i].lstrip('1'))
            if cnt == 0:
                i += 1
            elif 2 <= cnt <= 4:
                while i + 1 < n and arr[i + 1].startswith('10') and cnt > 1:
                    i += 1
                    cnt -= 1
                if cnt != 1:
                    return False
                i += 1
            else:
                return False
        return True
```
