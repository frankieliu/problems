
2-liner in Python. Optimization and tricks explained.

https://leetcode.com/problems/partition-equal-subset-sum/discuss/90658

* Lang:    python3
* Author:  o_sharp
* Votes:   1

```
class Solution(object):
    def canPartition(self, nums):
        s, mod = divmod(sum(nums), 2)
        return reduce(lambda dp,n:[v or i+n<=s and dp[i+n] for i,v in enumerate(dp)],nums,[False]*s+[not mod])[0]
```

If you prefer not using ```reduce```, here is a 5-liner:
```
class Solution(object):
    def canPartition(self, nums):
        target, invalid = divmod(sum(nums), 2)
        dp = [False]*target + [not invalid]
        for n in nums:
            dp = [v or i+n<=target and dp[i+n] for i,v in enumerate(dp)]
        return dp[0]
```

A faster version that avoids some computation is:
```
class Solution(object):
    def canPartition(self, nums):
        target, invalid = divmod(sum(nums), 2)
        dp = [False]*target + [not invalid]
        for n in nums*(1-invalid):
            dp = [v or i+n<=target and dp[i+n] for i,v in enumerate(dp)]
        return dp[0]
```

To make the code short, here are some tricks:
1. ```divmod``` is used.
2. More importantly, ```dp``` array should be reversed, where ```dp[0]``` stores the value for sum ```target```, ```dp[1]``` stores the value for ```target-1```...```dp[values]``` stores the value for ```0```
That's why we return dp[0] in the end.

For the reference, this is a standard implementation where the concise version comes:
```
class Solution(object):
    def canPartition(self, nums):
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        dp = [True] + [False]*target
        for n in nums:
            for s in range(target, n-1, -1):
                dp[s] = dp[s] or dp[s-n]
        return dp[-1]
```

@StefanPochmann How do you like this one? :-)
