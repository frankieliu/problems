
Accepted Python solution

https://leetcode.com/problems/range-sum-query-immutable/discuss/75292

* Lang:    python3
* Author:  Ushiao
* Votes:   2

This solution is not a O(N) look at the comment "# No O(N) cause", i don't know why, can't use "nums[0]" before loop, i got error out of range, so stranger!
    
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.lists = [0]
        # error out of range when use nums[0] here
        # nums[0]
        for i, n in enumerate(nums):
            # No O(N) cause
            if i == 0:
                self.lists.append(nums[i])
            else:
                self.lists.append(self.lists[i] + n)
            
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.lists[j+1] - self.lists[i]
