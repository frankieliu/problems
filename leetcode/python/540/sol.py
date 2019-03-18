
Python solution using set (slow not recommended)

https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100785

* Lang:    python3
* Author:  kang-li
* Votes:   0

The first solution I came up with and saw that it has not been posted here yet. It was accepted but is not a O(log n) solution. Perhaps something needs to be done so that such a solution will not be accepted? More generally, is this an efficient approach if the O(log n) constraint is not specified? 
```
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in set(nums):
            if (nums.count(n)!=2):
                return n
```
