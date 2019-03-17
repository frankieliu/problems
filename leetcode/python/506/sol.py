
My python solution

https://leetcode.com/problems/relative-ranks/discuss/98501

* Lang:    python3
* Author:  yang_fan
* Votes:   0

The explaination is as below
```
def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #use sorted to creat a new rank array
        #because the sorted list is form small to the large number so we have to use the tail of the array
        #A better solution is to reverse the rank so that count from the head
        result=[]
        rank=sorted(nums)
        for i in range(len(nums)):
            if rank.index(nums[i])==len(nums)-1:
                result.append('Gold Medal')
            elif rank.index(nums[i])==len(nums)-2:
                result.append('Silver Medal')
            elif rank.index(nums[i])==len(nums)-3:
                result.append('Bronze Medal')
            else:result.append(str(len(nums)-rank.index(nums[i])))
        return result
```
