
No hashing no stack. Only a Python array.

https://leetcode.com/problems/daily-temperatures/discuss/109853

* Lang:    python3
* Author:  lebrave
* Votes:   0

```
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        lt = len(temperatures)
        if lt ==1:
            return [0]
        res = [0]*lt
        record = [0]*101
        for t in range(temperatures[-1]):
            record[t] = lt-1
        for i in range(lt-2, -1, -1):
            tpt= temperatures[i]      
            res[i]=max(record[tpt]-i,0)
            for j in range(tpt):
                record[j]=i
        return res
```
