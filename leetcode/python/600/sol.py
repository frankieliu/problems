
python dp solution easily understood

https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/discuss/103755

* Lang:    python3
* Author:  yawnzheng
* Votes:   5

```
class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        # A[0] is the lowest bit, A[-1] is the highest bit
        A=bin(num)[2:][::-1]
        # dp[i][0] is the number of integers with (i+1)bits, highest bit is 0 and without consecutive ones
        # dp[i][1] is the number of integers with (i+1)bits, highest bit is 1 and without consecutive ones
        dp=[[1,1] for _ in range(len(A))]
        # res is the number of integers less than A[:i] without consecutive ones.
        res=1 if A[0]=='0' else 2
        for i in range(1, len(A)):
            dp[i][0]=dp[i-1][0]+dp[i-1][1]
            dp[i][1]=dp[i-1][0]
            # try to get the number of integers less than A[:i+1]
            if A[i-1:i+1]=='01':
                # if A[i-1:i+1]=='01', we can append '1' after integers less than A[:i] without consecutive ones, 
                # also any integer with (i+1) bits, highest bit is '0', without consecutive ones
                # is less than A[:i+1]
                res+=dp[i][0]
            elif A[i-1:i+1]=='11':
                # if A[i-1:i+1]=='11', then any integer with i+1 bits and without consecutive ones 
                # is less than A[:i+1]
                res=dp[i][0]+dp[i][1]
            # if A[i]=='0', the number of integers  with i+1 bits, less than A[:i+1]  and without 
            # consecutive ones is the same as A[:i]
        return res
```
