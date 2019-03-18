
Simple python solution with dictionary

https://leetcode.com/problems/longest-harmonious-subsequence/discuss/103504

* Lang:    python3
* Author:  yang_fan
* Votes:   0

First use **counter** function to record each **number as key** and the **frequency of occurences as value**, then go through the dictionary to search the **+1** or **-1** pairs, return the maximum of frequency sum.
```
 def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic=collections.Counter(nums)
        result=0
        for key in dic:
            if (key+1) in dic:
                s=dic[key]+dic[key+1]
                result=max(result,s)
            elif (key-1) in dic:
                s=dic[key]+dic[key-1]
                result=max(result,s)
        return result
```
