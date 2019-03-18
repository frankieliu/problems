
Python solution using dictionary

https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/100172

* Lang:    python3
* Author:  Billsad
* Votes:   0

```
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = []
        dict = {}
        for i in xrange(len(nums)):
            if nums[i] in dict:
                count.append((dict[nums[i]],nums[i]))
            dict[nums[i]+k] = nums[i]
        return len(set(count))

````
