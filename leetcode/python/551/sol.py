
Straight forward python solution

https://leetcode.com/problems/student-attendance-record-i/discuss/101576

* Lang:    python3
* Author:  yang_fan
* Votes:   0

I use maxcountL to count the max continuous late time. Others are straight forward.
```
def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA,countL,maxcountL=0,0,0
        for st in s:
            if st=='L':
                countL+=1
                maxcountL=max(maxcountL,countL)
            else:countL=0
            if st=='A':countA+=1
        return (countA<=1 and maxcountL<=2)
```
