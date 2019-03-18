
Easy to understand python solution

https://leetcode.com/problems/max-consecutive-ones/discuss/96792

* Lang:    python3
* Author:  yang_fan
* Votes:   0

Count the consecutive ones and store each count into the counts list. In detail, once the consecutive ones stop, save the count into the list and clear the count as zero, return the maximum of the counts list.
```
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count=count+1
            else:
                counts.append(count)
                count=0
        counts.append(count)
        return max(counts)
```
