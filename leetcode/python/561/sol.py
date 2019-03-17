
Pretty easy python solution with explaination

https://leetcode.com/problems/array-partition-i/discuss/102221

* Lang:    python3
* Author:  yang_fan
* Votes:   0

For example, input [1,4,3,2], to make the the largest sum of min(ai, bi), the target pairs should be (1,2) and (3,4). Let's see the hidden pattern inside. If each pair (ai, bi) contains the neighbors in the sorted array, the sum of each min can be the largest. And then the solution is written straight forward with the idea\uff0cjust add the odd index of sorted array to the sum and report. 
```
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s,i=0,0
        while i<len(nums):
            s+=nums[i]
            i+=2
        return s
```
